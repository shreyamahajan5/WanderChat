import os
import streamlit as st
import google.generativeai as genai

# ====== Set page config ======
st.set_page_config(page_title="WanderChat", page_icon="🌍", layout="wide")

# ====== Load Gemini API Key ======
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ====== Background Image Styling ======
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("/Users/shreyamahajan/Downloads/WanderChat_Streamlit_Gemini/photo.jpeg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .main-content {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        margin: 2rem auto;
        border-radius: 16px;
        width: 80%;
        max-width: 800px;
        backdrop-filter: blur(6px);
    }

    .block-container {
        padding-top: 2rem;
    }

    .title-text {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
    }

    .subtitle-text {
        text-align: center;
        font-size: 1.2rem;
        color: #333;
    }

    .chat-input {
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ====== Gemini Chat Setup ======
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# ====== UI Title ======
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown('<div class="title-text">🌍 WanderChat</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Ask travel tips, places to visit, local weather, and more!</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ====== Chat History Storage ======
if "messages" not in st.session_state:
    st.session_state.messages = []

# ====== Show Chat History ======
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ====== Chat Input ======
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
