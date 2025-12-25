import streamlit as st
import requests
import os

st.set_page_config(page_title="ExposureIQ - LangChain Chat", layout="wide")

st.title("🔍 ExposureIQ - LangChain Assistant")
st.markdown("Chat with your LangChain-powered AI assistant")

# Backend URL configuration
backend_url = os.getenv("BACKEND_URL", "http://localhost:8080")

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
    
    # Call FastAPI backend
    try:
        with st.spinner("Thinking..."):
            response = requests.post(
                f"{backend_url}/chat",
                json={"text": user_input},
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            assistant_reply = data.get("reply", "No response from backend")
            
        # Add assistant message to history
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        st.chat_message("assistant").write(assistant_reply)
        
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error connecting to backend: {str(e)}")
        st.info(f"Backend URL: {backend_url}")

# Sidebar with info
with st.sidebar:
    st.markdown("### ℹ️ About")
    st.markdown("""
    This is a **LangChain Chat** interface powered by:
    - **Frontend:** Streamlit
    - **Backend:** FastAPI + LangChain
    - **LLMs:** GROQ, OpenAI, or other providers
    """)
    
    st.markdown("---")
    st.markdown("### 🔌 Backend Status")
    try:
        health = requests.get(f"{backend_url}/health", timeout=5).json()
        st.success(f"✅ Backend online")
    except:
        st.error(f"❌ Backend offline")
        st.code(f"URL: {backend_url}", language="text")
