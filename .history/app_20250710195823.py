import streamlit as st
import os
import google.generativeai as genai
import base64

def set_bg_image(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}

    .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 12px;
        backdrop-filter: blur(6px);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Get your Gemini API key from env variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ GEMINI_API_KEY is not set in your environment.")
    st.stop()

genai.configure(api_key=api_key)

# Load Gemini model (chat mode)
model = genai.GenerativeModel("gemini-1.5-pro")

# Setup Streamlit
st.set_page_config(page_title="WanderChat", page_icon="🌍")
st.title("🌍 WanderChat")
set_bg_image("photo.jpeg")

st.caption("Ask travel tips, places to visit, local weather, and more!")

# Initialize chat in session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask me anything about a place...")
if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    try:
        response = st.session_state.chat.send_message(user_input)
        reply = response.text
    except Exception as e:
        reply = "❌ Error: " + str(e)

    # Show assistant message
    st.chat_message("assistant").markdown(reply)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})


