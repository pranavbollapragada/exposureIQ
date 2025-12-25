# ExposureIQ — LangChain Streamlit App

This is a Streamlit-based LangChain chat interface.

## Quick start (local)

1. Copy `.env.example` → `.env` and fill in your API keys.
2. `pip install -r requirements.txt`
3. `streamlit run streamlit_app.py`
4. Open http://localhost:8501 in your browser

## Features

- Chat interface with conversation history
- Environment variable support for API keys (LANGCHAIN_API_KEY, GROQ_API_KEY, OPENAI_API_KEY, TAVILY_API_KEY)
- API key status indicator in sidebar
- Clear chat history button

## Deployment

See `DEPLOY.md` for instructions on hosting to Hugging Face Spaces.

## Notes

- **Do not** commit `.env` with real keys.
- The chat response is currently a placeholder; replace with your LangChain chain logic.
