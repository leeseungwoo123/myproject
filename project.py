import streamlit as st

#웹 페이지의 제목
st.title("공동교육과정")

pages={'카테고리명1':
       [st.Page('login.py',title='A페이지'),
        st.Page('b.py',title='B페이지')],
    '카테고리명2': [st.Page('c.py',title='C페이지'),
                   st.Page('d.py',title='D페이지')]}

pg=st.navigation(pages)
pg.run()


img=st.image('죠르디.png')







