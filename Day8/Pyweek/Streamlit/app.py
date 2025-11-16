# streamlit run app.py

import streamlit as st
import requests
from audio_player import play_audio_from_base64

# Backend API URL
BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="AI Bot", page_icon="🤖", layout="centered")

st.title("🤖 AI Bot Assistant")
st.write("Ask anything and get text + audio response!")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input section
user_input = st.text_area("Your Question:", placeholder="Type your question here...", height=100)

col1, col2 = st.columns([1, 5])
with col1:
    submit_button = st.button("Ask AI 🚀", use_container_width=True)
with col2:
    clear_button = st.button("Clear History 🗑️", use_container_width=True)

if clear_button:
    st.session_state.chat_history = []
    st.rerun()

# Handle submission
if submit_button and user_input.strip():
    with st.spinner("Thinking... 🤔"):
        try:
            response = requests.post(
                f"{BACKEND_URL}/askAI",
                json={"text_input": user_input}
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Add to chat history
                st.session_state.chat_history.append({
                    "question": user_input,
                    "answer": data["text_output"],
                    "audio": data["text_audio"]
                })
                
                st.success("Response received! ✅")
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection error: {str(e)}")

# Display chat history
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("💬 Conversation History")
    
    for i, chat in enumerate(reversed(st.session_state.chat_history)):
        with st.container():
            st.markdown(f"**Q{len(st.session_state.chat_history)-i}:** {chat['question']}")
            st.markdown(f"**A:** {chat['answer']}")
            
            # Play audio if available
            if chat['audio']:
                play_audio_from_base64(chat['audio'], key=f"audio_{i}")
            
            st.markdown("---")
