import streamlit as st
import requests

API_KEY = "sk-std-Y0bUYWPi-Iw0v_7kQ0jJc26FMndV86VCb7fGKAekg4k"
URL = "https://server.iac.ac.il/api/v1/studentapi/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}"}

st.set_page_config(page_title="צ'אט AI", page_icon="💬")
st.title("💬 צ'אט עם AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if st.button("נקה שיחה"):
    st.session_state.messages = []
    st.rerun()

if user_input := st.chat_input("כתבי הודעה..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("חושב..."):
            payload = {
                "messages": st.session_state.messages,
                "max_completion_tokens": 1000
            }
            response = requests.post(URL, json=payload, headers=headers)
            answer = response.json()["choices"][0]["message"]["content"]
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})