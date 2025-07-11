import os
import streamlit as st
import google.generativeai as genai
import base64

# ========== CONFIG ==========
st.set_page_config(page_title="WanderChat", page_icon="🌍", layout="wide")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
chat = model.start_chat(history=[])

# ========== Load image as base64 ==========
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_base64 = get_base64_image("images/photo.jpeg")

# ========== CSS (NO white box now) ==========
st.markdown(f"""
    <style>
    .stApp {{
            
        background-image: url("data:image/jpeg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Segoe UI', sans-serif;
    }}

    .block-container {{
        padding-top: 0 !important;
    }}

    .title {{
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-top: 3rem;
        color: #ffffff;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }}

    .subtitle {{
        text-align: center;
        font-size: 1.25rem;
        color: #f0f0f0;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.4);
        margin-bottom: 2rem;
    }}

    .stChatMessage {{
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
    }}
    </style>
""", unsafe_allow_html=True)

# ========== UI ==========
st.markdown('<div class="title">🌍 WanderChat</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask travel tips, places to visit, local weather, and more!</div>', unsafe_allow_html=True)
# ====== Sidebar: Project Info ======

st.sidebar.markdown("## ℹ️ Project Info")
st.sidebar.markdown("""
**🔹 WanderChat: A Travel Chatbot**  
*Content-Based Filtering | React Frontend | Streamlit*

- Developed a virtual travel companion using content-based filtering.
- Built with a React front-end and Python backend.
- Proposed a recommendation system for:
  - 🏨 Accommodation  
  - 🚕 Transportation  
  - 🗺️ Tourist Attractions  
  - 🍽️ Food
- Recently updated with LLM integration for smarter responses.
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask me anything about a place...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            response = chat.send_message(user_input)
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error: {e}")
