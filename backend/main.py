import logging
import os
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag import answer_question

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
)
logger = logging.getLogger(__name__)

for _var in ["GROQ_API_KEY", "JINA_API_KEY", "QDRANT_URL", "QDRANT_API_KEY"]:
    if not os.getenv(_var):
        raise EnvironmentError(f"STARTUP ERROR: required env var '{_var}' is not set. Halting.")

app = FastAPI(title="CS11 Book API — Robo", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://faizanalifsd.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str
    selected_text: str = ""


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    sections: list[dict] = []


@app.get("/")
async def root():
    return {"status": "CS11 Book API is running", "docs": "/docs"}


@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    q = request.question.strip()
    if not q:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    logger.info(f"Q: {q[:120]}")

    try:
        result = await answer_question(q, request.selected_text)
    except RuntimeError as e:
        logger.error(f"LLM failure: {e}", exc_info=True)
        raise HTTPException(status_code=503, detail="AI service temporarily unavailable. Please try again.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")

    logger.info(f"Answer delivered. Sources: {result['sources']}")
    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"],
        sections=result.get("sections", []),
    )


@app.post("/verify-token")
async def verify_token(authorization: str = Header(...)):
    """Verify a JWT bearer token. Requires JWT_SECRET env var set in Vercel."""
    from jose import JWTError, jwt

    secret = os.getenv("JWT_SECRET")
    if not secret:
        raise HTTPException(status_code=503, detail="Auth service not configured — set JWT_SECRET")

    token = authorization.removeprefix("Bearer ").strip()
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return {"valid": True, "user": payload}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    """Create a Stripe checkout session. Requires STRIPE_SECRET_KEY env var set in Vercel."""
    import stripe as stripe_lib

    stripe_key = os.getenv("STRIPE_SECRET_KEY")
    if not stripe_key:
        raise HTTPException(status_code=503, detail="Payment service not configured — set STRIPE_SECRET_KEY")

    stripe_lib.api_key = stripe_key
    body = await request.json()
    price_id = body.get("price_id")
    if not price_id:
        raise HTTPException(status_code=400, detail="price_id is required")

    success_url = body.get("success_url", "https://faizanalifsd.github.io/computer-science-11-year/")
    cancel_url = body.get("cancel_url", "https://faizanalifsd.github.io/computer-science-11-year/")

    try:
        session = stripe_lib.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{"price": price_id, "quantity": 1}],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return {"session_id": session.id, "url": session.url}
    except Exception as e:
        logger.error(f"Stripe error: {e}")
        raise HTTPException(status_code=500, detail="Failed to create checkout session")


@app.post("/stripe-webhook")
async def stripe_webhook(request: Request):
    """Handle Stripe webhook events. Requires STRIPE_SECRET_KEY + STRIPE_WEBHOOK_SECRET env vars."""
    import stripe as stripe_lib

    stripe_key = os.getenv("STRIPE_SECRET_KEY")
    webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
    if not stripe_key or not webhook_secret:
        raise HTTPException(status_code=503, detail="Webhook not configured — set STRIPE_SECRET_KEY and STRIPE_WEBHOOK_SECRET")

    stripe_lib.api_key = stripe_key
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature", "")

    try:
        event = stripe_lib.Webhook.construct_event(payload, sig_header, webhook_secret)
    except stripe_lib.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid Stripe signature")

    event_type = event["type"]
    logger.info(f"Stripe event received: {event_type}")

    if event_type == "checkout.session.completed":
        session = event["data"]["object"]
        logger.info(f"Payment completed: {session['id']}")
        # TODO: update user access in Neon DB

    return {"received": True}
