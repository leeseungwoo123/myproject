import streamlit as st









pages={' ':[st.Page('login_page.py',title='로그인'),
st.Page('page1.py',title='메인'),st.Page('easy.py',title='쉬움'),
st.Page('normal.py',title='보통'),st.Page('hard.py',title='어려움')], }

pg=st.navigation(pages)
pg.run()




