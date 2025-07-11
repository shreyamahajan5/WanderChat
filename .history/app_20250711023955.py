
import streamlit as st
import os
import google.generativeai as genai

# Set your API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY environment variable not set.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

# Initialize model
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="WanderChat Gemini", page_icon="🌍")
st.title("🌍 WanderChat - Your Gemini Travel Chatbot")

st.sidebar.header("WanderChat Gemini")
st.sidebar.markdown("- Ask me about cities, landmarks, or trip tips!")
st.sidebar.markdown("- Try: 'What to do in Paris?' or 'Best season to visit Tokyo'")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
user_input = st.chat_input("Ask your travel question...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = model.generate_content(user_input)
        reply = response.text
        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.chat_message("assistant").error(f"Error: {str(e)}")
