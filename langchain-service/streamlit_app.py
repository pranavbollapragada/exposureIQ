import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="ExposureIQ - LangChain Chat", layout="wide")

st.title("🔍 ExposureIQ - LangChain Assistant")
st.markdown("Chat with your LangChain-powered AI assistant")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
st.markdown("---")
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Chat input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    # TODO: Wire LangChain here
    # Example: use GROQ_API_KEY, OPENAI_API_KEY, TAVILY_API_KEY, LANGCHAIN_API_KEY
    with st.spinner("Thinking..."):
        # Placeholder response
        assistant_reply = f"(Placeholder) You said: {user_input}"
    
    # Add assistant message to history
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    st.chat_message("assistant").write(assistant_reply)

# Sidebar with info and settings
with st.sidebar:
    st.markdown("### ℹ️ About")
    st.markdown("""
    This is a **LangChain Chat** interface powered by:
    - **Streamlit** web UI
    - **LangChain** for chains
    - **GROQ**, OpenAI, or other LLMs
    - **Tavily** for web search (optional)
    """)
    
    st.markdown("---")
    st.markdown("### 🔑 API Keys Loaded")
    keys_status = {
        "LANGCHAIN_API_KEY": bool(os.getenv("LANGCHAIN_API_KEY")),
        "GROQ_API_KEY": bool(os.getenv("GROQ_API_KEY")),
        "OPENAI_API_KEY": bool(os.getenv("OPENAI_API_KEY")),
        "TAVILY_API_KEY": bool(os.getenv("TAVILY_API_KEY")),
    }
    
    for key, loaded in keys_status.items():
        status = "✅" if loaded else "❌"
        st.write(f"{status} {key}")
    
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
