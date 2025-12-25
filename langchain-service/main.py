from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="ExposureIQ - LangChain Service")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "LangChain service ready"}


class Message(BaseModel):
    text: str


@app.post("/chat")
async def chat(msg: Message):
    # Minimal guard: require an LLM API key to be set in env
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        raise HTTPException(status_code=400, detail="OPENAI_API_KEY not set in environment (or use another LLM provider)")

    # TODO: wire LangChain LLM/chain here using the env key(s)
    # This is intentionally a placeholder to keep the scaffold minimal and safe.
    return {"input": msg.text, "reply": "(placeholder) LLM reply would appear here when configured."}
