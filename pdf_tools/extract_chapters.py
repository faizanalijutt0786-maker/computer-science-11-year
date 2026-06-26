"""
CS11 Book PDF Extractor — uses PyMuPDF + EasyOCR for scanned PDF pages.
Run from project root:
    python pdf_tools/extract_chapters.py
"""
import os, re, sys, warnings, logging
import fitz
from PIL import Image

logging.getLogger("pdfminer").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

PDF_PATH  = os.path.join(os.path.dirname(__file__), "..", "computer 11 SC 20-6-2025 1_Compressed.pdf")
DOCS_DIR  = os.path.join(os.path.dirname(__file__), "..", "my-website", "docs", "computer-science-11")
RENDER_DPI = 220

CHAPTERS = [
    (2, "Python Programming",                    "chapter-2",  23,  43),
    (3, "Algorithms and Problem Solving",         "chapter-3",  44,  58),
    (4, "Computational Structures",               "chapter-4",  59,  69),
    (5, "Data Analytics",                         "chapter-5",  70,  88),
    (6, "Emerging Technologies",                  "chapter-6",  89, 103),
    (7, "Legal and Ethical Aspects of Computing", "chapter-7", 104, 117),
    (8, "Online Research and Digital Literacy",   "chapter-8", 118, 127),
    (9, "Entrepreneurship in Digital Age",        "chapter-9", 128, 144),
]

WATERMARK = {"web version of pectaa", "not for sale", "web version", "not for", "pectaa"}

def load_ocr():
    import easyocr
    print("Loading EasyOCR model (first run downloads ~100 MB)...")
    reader = easyocr.Reader(["en"], gpu=False, verbose=False)
    print("EasyOCR ready.")
    return reader

def ocr_page(reader, page) -> str:
    mat = fitz.Matrix(RENDER_DPI / 72, RENDER_DPI / 72)
    pix = page.get_pixmap(matrix=mat, colorspace=fitz.csGRAY)
    img_bytes = pix.tobytes("png")
    results = reader.readtext(img_bytes, detail=0, paragraph=True)
    lines = []
    for line in results:
        if line.strip().lower() not in WATERMARK:
            lines.append(line)
    return "\n".join(lines)

def clean_text(raw: str) -> str:
    lines = raw.splitlines()
    out = []
    for line in lines:
        s = line.strip()
        if re.fullmatch(r"\d{1,3}", s):
            continue
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def build_markdown(num: int, title: str, body: str) -> str:
    return f"""---
id: chapter-{num}
title: "Chapter {num}: {title}"
sidebar_label: "Chapter {num}: {title}"
sidebar_position: {num}
---

# Chapter {num}: {title}

{body}
"""

def extract_chapter(reader, doc, num, title, slug, start, end):
    parts = []
    for i in range(start - 1, end):
        text = ocr_page(reader, doc[i])
        cleaned = clean_text(text)
        if cleaned:
            parts.append(cleaned)
        sys.stdout.write(f"\r  page {i+1}/{end} done")
        sys.stdout.flush()
    print()
    body = "\n\n---\n\n".join(parts)
    md   = build_markdown(num, title, body)
    path = os.path.join(DOCS_DIR, f"{slug}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    return path, len(md)

def main():
    if not os.path.exists(PDF_PATH):
        sys.exit(f"PDF not found: {PDF_PATH}")
    os.makedirs(DOCS_DIR, exist_ok=True)

    # find the next chapter not yet extracted (skip empty placeholder files)
    next_chapter = None
    for idx, (num, title, slug, start, end) in enumerate(CHAPTERS):
        path = os.path.join(DOCS_DIR, f"{slug}.md")
        size = os.path.getsize(path) if os.path.exists(path) else 0
        if size < 500:  # empty or near-empty = not done
            next_chapter = (idx, num, title, slug, start, end)
            break

    if next_chapter is None:
        print("All chapters already extracted!")
        print("Next step: cd backend && python indexer.py")
        return

    idx, num, title, slug, start, end = next_chapter
    total = len(CHAPTERS)
    done  = idx

    print(f"Progress: {done}/{total} chapters done")
    print(f"Extracting Chapter {num}: {title} (pages {start}-{end})...")
    print("(OCR is slow: ~1-2 min per page on CPU)\n")

    reader = load_ocr()
    doc    = fitz.open(PDF_PATH)
    path, chars = extract_chapter(reader, doc, num, title, slug, start, end)
    doc.close()

    print(f"\n[DONE] Chapter {num}: {title}")
    print(f"   Saved: {path}  ({chars:,} chars)")
    print(f"   Progress: {done+1}/{total} chapters done")

    if done + 1 < total:
        next_num, next_title, *_ = CHAPTERS[done + 1]
        print(f"\n   Run the script again for Chapter {next_num}: {next_title}")
    else:
        print("\n[ALL DONE] All chapters extracted! Next: cd backend && python indexer.py")

if __name__ == "__main__":
    main()
