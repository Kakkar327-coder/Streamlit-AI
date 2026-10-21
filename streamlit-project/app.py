import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(page_title="Smart AI Assistant", page_icon="🔥", layout="centered")

st.title("🔥 Smart AI Assistant")
st.write("Ask anything — AI responds in your style!")

# Sidebar configuration for API key and model selection
with st.sidebar:
    st.header("⚙️ Settings")
    env_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GENAI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
    api_key = st.text_input(
        "Google Gemini API Key:",
        value=env_key,
        type="password",
        help="Get an API key from Google AI Studio (https://aistudio.google.com/)"
    )
    model = st.selectbox(
        "Select Model:",
        ["gemini-2.5-flash", "gemini-3.8-flash"],
        index=0
    )

user_input = st.text_input("Enter your question:")

tone = st.selectbox(
    "Choose response style:",
    ["Normal", "Funny", "Strict Teacher", "Motivational"]
)

if st.button("Generate"):
    if not user_input:
        st.warning("Please enter a question!")
    elif not api_key or api_key.strip() == "API_KEY_HERE":
        st.error("Please enter a valid Gemini API key in the sidebar or set the GEMINI_API_KEY environment variable.")
    else:
        prompt = f"Answer this question in a {tone} style: {user_input}"
        try:
            with st.spinner("Generating response..."):
                client = genai.Client(api_key=api_key.strip())
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
            st.success("Response generated!")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error generating response: {e}")