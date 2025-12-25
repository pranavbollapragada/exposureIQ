# ExposureIQ — LangChain scaffold

This folder contains a minimal FastAPI scaffold intended to host a LangChain-based service.

Quick start (local):

1. Copy `.env.example` to `.env` and fill in your keys.
2. pip install -r requirements.txt
3. uvicorn main:app --reload --port 8080

Endpoints:
- GET `/health` — health check
- POST `/chat` — placeholder chat endpoint (requires `OPENAI_API_KEY` by default)

Notes:
- **Do not** commit real API keys — use GitHub Secrets or your host's secret manager.
- The `/chat` endpoint is a placeholder; replace with your LangChain chains and vector store initialization as needed.
