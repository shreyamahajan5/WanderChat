import os
import base64
import streamlit as st
import google.generativeai as genai

# ====== Set page config ======
st.set_page_config(page_title="WanderChat", page_icon="🌍", layout="wide")

# ====== Load Gemini API Key ======
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ====== Function to embed local image as background ======
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
        }}

        .main-content {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            margin: 2rem auto;
            border-radius: 16px;
            width: 90%;
            max-width: 900px;
            color: white;
            backdrop-filter: blur(6px);
            text-align: center;
        }}

        .title-text {{
            font-size: 2.8rem;
            font-weight: bold;
        }}

        .subtitle-text {{
            font-size: 1.2rem;
            margin-top: 0.5rem;
            color: #ddd;
        }}

        .block-container {{
            padding-top: 2rem;
        }}

        .stChatMessage {{
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ====== Set your background image path here ======
set_background("images/photo.jpeg")  # Must be in the same folder as app.py

# ====== Gemini Chat Setup ======
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
chat = model.start_chat(history=[])


# ====== UI Title ======
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown('<div class="title-text">🌍 WanderChat</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Ask travel tips, places to visit, local weather, and more!</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ====== Chat History State ======
if "messages" not in st.session_state:
    st.session_state.messages = []

# ====== Display Chat History ======
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ====== Chat Input and Reply ======
prompt = st.chat_input("Ask me anything about a place...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = chat.send_message(prompt)
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error: {e}")
