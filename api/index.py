import sys
import os

# Vercel runs from project root; backend/ is not on sys.path by default.
# This line makes `from rag import ...` and `from embeddings import ...` resolve correctly.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from main import app  # noqa: F401 — Vercel discovers the ASGI app via this name
