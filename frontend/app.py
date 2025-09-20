import streamlit as st
from genai_client import GenAIClient  # ✅ no more utils path issue

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Gemini Chatbot")

# Sidebar for settings
st.sidebar.header("⚙️ Settings")
model = st.sidebar.selectbox(
    "Choose a model",
    ["gemini-1.5-flash", "gemini-1.5-pro"],  # ✅ only valid models
    index=0
)
max_tokens = st.sidebar.slider("Max tokens", 64, 1024, 256)

# Input box
prompt = st.text_area("Enter your prompt:")

# Button
if st.button("Generate"):
    if prompt.strip():
        client = GenAIClient()
        with st.spinner("Generating response..."):
            reply = client.generate_reply(prompt, model=model, max_tokens=max_tokens)
        st.success("Response:")
        st.write(reply)
    else:
        st.warning("⚠️ Please enter a prompt first!")
