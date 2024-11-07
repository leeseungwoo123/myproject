import streamlit as st

st.set_page_config(page_title="login")


st.title('로그인')
id=st.text_input('아이디')
pw=st.text_input('비밀번호',type='password')
btn=st.button('확인')

if btn:
    if id=='abc'and pw=='123':
        st.success("로그인 성공")
        st.switch_page('page1.py')
    else:
        st.error("로그인 실패")

