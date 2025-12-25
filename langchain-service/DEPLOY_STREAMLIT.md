# Deploying the ExposureIQ Streamlit App

## Option 1: Hugging Face Spaces (Recommended, Free)

Easiest & fastest for Streamlit apps.

### Steps:

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in:
   - **Space name:** `exposureiq-langchain` (or your choice)
   - **License:** Choose one (e.g., MIT)
   - **Space SDK:** `Streamlit`
   - **Visibility:** Public or Private
4. Click **"Create Space"**
5. In the Space settings (**Settings** tab):
   - Go to **"Repository secrets"**
   - Add your secrets:
     - `LANGCHAIN_API_KEY`
     - `GROQ_API_KEY`
     - `OPENAI_API_KEY`
     - `TAVILY_API_KEY`
6. Upload files to the Space repo:
   ```bash
   git clone https://huggingface.co/spaces/<your-username>/exposureiq-langchain
   cd exposureiq-langchain
   cp <path-to-exposureiq-repo>/langchain-service/* .
   git add .
   git commit -m "Add ExposureIQ app"
   git push
   ```
7. Space will auto-deploy. Visit `https://huggingface.co/spaces/<your-username>/exposureiq-langchain` to see it live!

---

## Option 2: Streamlit Cloud (Free, Official)

Also great for Streamlit apps.

### Steps:

1. Go to https://streamlit.io/cloud
2. Click **"Deploy an app"** → **"Paste GitHub repo URL"**
3. Paste: `https://github.com/pranavbollapragada/exposureIQ`
4. Fill in:
   - **Branch:** `main`
   - **Main file path:** `langchain-service/streamlit_app.py`
5. Click **"Deploy"**
6. Once deployed, go to **Settings** (gear icon):
   - Add **Secrets** (same as HF Spaces):
     - `LANGCHAIN_API_KEY`
     - `GROQ_API_KEY`
     - `OPENAI_API_KEY`
     - `TAVILY_API_KEY`
7. Done! App is live at the provided URL.

---

## Summary

| Host | Cost | Ease | Speed |
|------|------|------|-------|
| **HF Spaces** | Free | Easy | ~1 min |
| **Streamlit Cloud** | Free | Easy | ~2 min |

**Recommendation:** Use **Hugging Face Spaces** or **Streamlit Cloud** for simplicity.
