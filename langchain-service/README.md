# ExposureIQ — LangChain scaffold

This folder contains a FastAPI backend + Streamlit frontend for a LangChain-based service.

## Quick start (local)

1. Copy `.env.example` -> `.env` and fill in your keys.
2. `pip install -r requirements.txt`
3. **Terminal 1 (Backend):**
   - `uvicorn main:app --reload --port 8080`
4. **Terminal 2 (Frontend):**
   - `streamlit run streamlit_app.py --server.port 8501`
5. Open http://localhost:8501 in your browser

## Endpoints

**Backend (FastAPI):**
- GET `/health` — health check
- GET `/` — service info
- POST `/chat` — chat endpoint (requires `OPENAI_API_KEY` by default)

**Frontend (Streamlit):**
- Web UI at http://localhost:8501
- Calls backend at `http://localhost:8080` (configurable via `BACKEND_URL` env var)

## Notes

- **Do not** commit real API keys — use GitHub Secrets or host's secret manager.
- The `/chat` endpoint is a placeholder; replace with your LangChain chains and vector store as needed.
- Streamlit frontend connects to FastAPI backend via HTTP.
