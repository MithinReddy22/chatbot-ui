import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="ReddyBot 💬", page_icon="🤖")

st.title("🤖 ReddyBot – Your AI Chat Partner")
st.markdown("Built with [DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium)")

# Load model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input from user
user_input = st.text_input("You:", key="input")

if user_input:
    response = chatbot(user_input, max_length=100)[0]["generated_text"]
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"🧑‍💻 **You:** {msg}")
    else:
        st.markdown(f"🤖 **ReddyBot:** {msg}")


