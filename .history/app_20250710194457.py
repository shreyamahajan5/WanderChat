import streamlit as st
import os
import google.generativeai as genai

# Load Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY environment variable not set.")
    st.stop()

genai.configure(api_key=api_key)

# Setup the Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")  # correct model name
chat = model.start_chat(history=[])

st.title("🌍 WanderChat - Powered by Gemini")
st.sidebar.markdown("Ask travel-related questions like:\n- What to do in Tokyo?\n- Best time to visit Iceland")

# Session state to maintain chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for entry in st.session_state.chat_history:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])

user_input = st.chat_input("Where would you like to explore?")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    try:
        response = chat.send_message(user_input)
        reply = response.text
    except Exception as e:
        reply = f"Error: {str(e)}"

    st.chat_message("assistant").markdown(reply)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
