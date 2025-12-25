# Deploying the LangChain Service

This document explains how to publish and run the `langchain-service`.

1) Secrets and environment variables
   - Do NOT commit `.env` with real keys.
   - Locally: copy `.env.example` -> `.env` and fill in values.
   - For CI / deploy: set these repository secrets in GitHub: `OPENAI_API_KEY`, `LANGCHAIN_API_KEY`, `GROQ_API_KEY`, `TAVILY_API_KEY`.

2) GitHub Actions
   - On push to `main`, the workflow will run tests and build a Docker image and push it to GitHub Container Registry (`ghcr.io/<owner>/<repo>/langchain-service:latest`).
   - To automatically deploy to Google Cloud Run, add these secrets: `GCLOUD_SA_KEY` (service account JSON), `GCLOUD_PROJECT`, and `GCLOUD_REGION`.

   5) Helper script to set secrets
      - A simple PowerShell helper is available at `scripts/set-github-secrets.ps1` which reads a local `.env` and sets repo secrets via `gh` (you must run it locally and have `gh` authenticated).

3) Render / other hosts
   - If using Render, connect the repo in the Render dashboard and set the same environment variables in the service settings.
   - For Hugging Face Spaces (Gradio/Streamlit), use their repo and secret management; large models may require paid plans.

4) Local test
   - pip install -r requirements.txt
   - uvicorn main:app --reload --port 8080
