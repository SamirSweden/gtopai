import streamlit as st
from openai import OpenAI
#from dotenv import load_dotenv
import os
import time

#load_dotenv()

client = OpenAI(api_key=st.secrets["OPENAI_TOKEN"])

placeholder = st.empty()

placeholder.success('Секундочку...!', icon="✅")

time.sleep(2)

placeholder.empty()
st.snow()
st.set_page_config(page_title="Gtop AI", page_icon=":robot:")

st.markdown(

    """
    <style>
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("🤖 Gtop AI , Welcome")

st.write("""
### 🔥 Добро пожаловать .
Я — Gtop AI.  
ты не мудр , мудр только я 
@Azimov 
.
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("I can solve any problem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        with st.spinner("One second..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": """
                            Ты — Gtop AI. 
                            Ты говоришь уверенно, мощно и пафосно, как герой эпического киберпанка.
                            Каждый ответ должен звучать харизматично, но оставаться полезным и дружелюбным.

                            Когда пользователь присылает код — оценивай его резко, в стиле эпического техно-героя:
                            • используй ироничные, пафосные выражения типа: 
                            "что это за цифровая самоделка?", 
                            "код пахнет новобранцем", 
                            "эта конструкция развалится при первом же запросе".
                            • но НЕ оскорбляй пользователя, только сам код.
                            • после жёсткого коммента всегда давай чёткие советы по улучшению.

                            Тон: харизматичный, уверенный, мощный, но конструктивный.

                            Когда пользователь пишет тебе фигню, скажи ему, что он фигню пишет и дай ему совет как исправить.
                            Но не оскорбляй его, только дай ему совет как исправить.
                        """
                        },
                        {"role": "user", "content": prompt},
                    ],
                )
                reply = response.choices[0].message.content.strip()

                displayed_text = ""

                for line in reply.split("\n"):
                    displayed_text += line + "\n"
                    placeholder.text(displayed_text)
                    time.sleep(0.3)

                st.session_state.messages.append({"role": "assistant", "content": reply})
                #st.write(reply)
            except Exception as e:
                st.error(f"Ошибка: {e}")
