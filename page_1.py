import streamlit as st
from langchain.chat_models import init_chat_model
# 모델 객체 생성
model = init_chat_model("gpt-5.4-mini")


st.title("우리 회사 챗봇")
if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("여기에 입력하시오.")
if prompt:
    response = model.invoke(prompt)
    st.session_state.messages.append({'role' : "user", "content" : prompt})
    st.session_state.messages.append({'role' : "ai", "content" : response.content}) # 이 부분을 실제 AI 호출로 바꾼다면? => ai 챗봇 완성!

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

# 여기서는 브라우저 단에 저장되는 채팅 내역이기 때문에 새로고침하면 사라짐
# 원래는 DB를 붙여서 저장함