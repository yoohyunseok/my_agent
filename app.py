import streamlit as st
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# st.title("우리 회사 챗봇")

page_1 = st.Page("page_1.py", title = '1 페이지')

page_2 = st.Page("page_2.py", title = '2 페이지')

page_3 = st.Page("page_3.py", title = '3 페이지')

pages = st.navigation([page_1, page_2, page_3], position = 'top') # 각 버튼을 눌렀을 때 해당 페이지로 이동하게 해주는 네비게이터

pages.run()