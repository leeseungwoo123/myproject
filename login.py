import streamlit as st
st.title('로그인')

btn_c=st.button('C')
btn_d=st.button('D')

if btn_c:
    st.switch_page('c.py')

if btn_d:
    st.switch_page('d.py')



