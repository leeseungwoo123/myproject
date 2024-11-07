import streamlit as st

pages={' ':[st.Page('pages/login_page.py',title='로그인'),
st.Page('pages/page1.py',title='메인'),st.Page('pages/easy.py',title='쉬움'),
st.Page('pages/normal.py',title='보통'),st.Page('pages/hard.py',title='어려움')], }

pg=st.navigation(pages)
pg.run()




