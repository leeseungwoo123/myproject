import streamlit as st

색상 = st.radio('당신이 좋아하는 색상은?',
              ['빨강',"노랑","파랑"])
과목=st.selectbox("과목을 선택하세요",['확률과 통계','미분과 적분','기하와 백터'])
st.write('당신이 선택한 과목은 '+str(과목)+'입니다.')
과학=st.multiselect("과목을 선택하세요",['물리','화학','생물','지구과학'],max_selections=2)
st.video('https://www.youtube.com/watch?v=kWiCuklohdY&pp=ygUJ7YyM7J207I2s')

st.write("다음 중 프로그래밍에 대한 설명으로 가장 적절한 것은?")
결과=st.radio("보기",['1. python을 배운다','2. 10주동안 수업한다','3. 3번 결석해도 된다.','4. 재미없다.'])
btn=st.button('정답확인')
if btn:
    if 결과 =='1. python을 배운다':
        st.success("정답")
        st.balloons()
    else:
        st.error("오답")
slider=st.select_slider('반을 선택하세요',['1반','2반','3반','4반'])

짜장면=st.checkbox('짜장면 5000원')
짬뽕=st.checkbox('짬뽕 6000원')
탕수육=st.checkbox('탕수육 12000원')
a=0

if 짜장면:
    a+=5000
if 짬뽕:
    a+=6000
if 탕수육:
    a+=12000
if a!=0:
    st.write(str(a)+'원 입니다.')

st.title("title")
st.header("header")
st.subheader("subheader")
st.write("**이승우**님 안녕하세요")
st.write(":rainbow[함지고등학교]")

st.title('로그인')
id=st.text_input('아이디')
pw=st.text_input('비밀번호',type='password')
btn=st.button('확인')

if btn:
    if id=='abc'and pw=='123':
        st.success("로그인 성공")
    else:
        st.error("로그인 실패")