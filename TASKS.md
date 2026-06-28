stiyou# CS11 Book — Pending Tasks

## 1. Extract Chapters 2–9 (BLOCKER)
- [ ] Install easyocr on fast internet: `pip install easyocr`
- [ ] Delete empty chapter-2.md and chapter-3.md (they have no content)
- [ ] Run `python pdf_tools/extract_chapters.py` once per chapter (auto-detects next unextracted)
- [ ] Repeat until all 8 chapters done (ch2 → ch9)

## 2. Index All Chapters into Qdrant
- [ ] After all chapters extracted, run: `cd backend && python indexer.py`
- [ ] Verify Robo answers questions from multiple chapters

## 3. Deploy Backend
- [ ] Deploy FastAPI backend to Render or Koyeb (Procfile already present)
- [ ] Set all env vars on the platform: GROQ_API_KEY, JINA_API_KEY, QDRANT_URL, QDRANT_API_KEY, OPENROUTER_API_KEY
- [ ] Test /health endpoint on the live URL

## 4. Update ChatWidget Backend URL
- [ ] In `my-website/src/components/ChatWidget.jsx` line 5, change:
      `const BACKEND_URL = 'http://localhost:8000'`
      to the deployed backend URL (e.g. https://your-app.koyeb.app)

## 5. Tighten CORS
- [ ] In `backend/main.py` line 29, change `allow_origins=["*"]`
      to `allow_origins=["https://faizanalijutt0786-maker.github.io"]`

## 6. Stripe Paywall
- [ ] Create Stripe account and get API keys
- [ ] Add Stripe Checkout endpoint to FastAPI backend
- [ ] Issue JWT token on successful payment
- [ ] Store token in localStorage on frontend
- [ ] Lock chapters 2–9: check JWT before rendering, redirect to payment if missing
- [ ] Test full purchase flow in Stripe test mode
- [ ] Switch to Stripe live mode before launch

## 7. Add Author Photo
- [ ] Add real photo to `my-website/static/img/author.jpg`
- [ ] Replace avatar placeholder in `my-website/src/pages/about-author.jsx` with `<img src="/computer-science-11-year/img/author.jpg" />`

## 8. End-to-End Test & Launch
- [ ] Test full user journey: land → read ch1 → ask Robo → pay → read ch2+ → ask Robo
- [ ] Verify GitHub Pages deployment is live
- [ ] Switch Stripe to live mode
- [ ] Announce launch
