# 🌍 WanderChat: AI-Powered Travel Chatbot

📍 **Live Demo:** [https://wanderchat.streamlit.app/](https://wanderchat.streamlit.app/)

---

## 🧭 Introduction

**WanderChat** is a virtual travel assistant powered by AI that offers travelers a smart and personalized way to explore the world.

With a conversational interface and intelligent recommendations, WanderChat helps users:

- Discover destinations tailored to their interests
- Get tips on transportation, accommodations, attractions, and food
- Check live weather conditions
- Ask travel-related questions—anytime, anywhere

---

## 🤖 How It Works

WanderChat uses an LLM-powered chatbot interface to simulate human-like travel conversations.

Key Features:
- ✈️ Destination recommendations
- 🏨 Accommodation and transport suggestions
- 📍 Local attractions and dining options
- 🌦️ Real-time weather info
- 💬 Chat interface with natural language interaction

---

## 💡 Why AI Chatbot?

Using an AI chatbot brings many advantages to a travel website:

- **24/7 Support:** Helps users even outside business hours.
- **Personalized Experience:** Tailors responses based on user preferences.
- **Continuous Learning:** Improves over time with more interactions.
- **Better Engagement:** Replaces static forms with natural conversations.
- **Efficiency:** Automates bookings and answers, reducing manual workload.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python (OpenAI / Gemini LLM)
- **APIs:** Google Generative AI / OpenAI, Wikipedia, OpenWeather
- **UI:** Custom CSS for background, chat layout, and sidebar

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/shreyamahajan5/WanderChat.git
cd WanderChat

# Install dependencies
pip install -r requirements.txt

# Set API Key
export GEMINI_API_KEY="your-api-key"

# Run Streamlit
streamlit run app.py
