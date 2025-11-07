import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=st.secrets["OPENAI_TOKEN"])

st.title("🤖 Gtop AI , Welcome")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("I can solve any problem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("One second..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Ты умный, добрый ассистент братуха."},
                        {"role": "user", "content": prompt},
                    ],
                )
                reply = response.choices[0].message.content.strip()

                st.session_state.messages.append({"role": "assistant", "content": reply})
                st.write(reply)
            except Exception as e:
                st.error(f"Ошибка: {e}")
