import streamlit as st

import random

# 게임 설정

words = ["python", "streamlit", "hangman", "development", "chatgpt"]

secret_word = random.choice(words)

max_attempts = 6

# 세션 상태 초기화

if 'attempts' not in st.session_state:

    st.session_state.attempts = 0

    st.session_state.guessed_letters = []

    st.session_state.display_word = "_" * len(secret_word)

# 단어 추측 함수

def guess_letter(letter):

    if letter in st.session_state.guessed_letters:

        st.warning("이미 추측한 글자입니다.")

    elif letter in secret_word:

        st.session_state.guessed_letters.append(letter)

        st.session_state.display_word = "".join(

            [c if c in st.session_state.guessed_letters else "_" for c in secret_word]

        )

    else:

        st.session_state.guessed_letters.append(letter)

        st.session_state.attempts += 1

# UI 설정

st.title("행맨 게임")

st.write("단어를 추측하세요!")

# 현재 상태 표시

st.write("단어: ", " ".join(st.session_state.display_word))

st.write(f"틀린 시도: {st.session_state.attempts} / {max_attempts}")

st.write("추측한 글자: ", " ".join(st.session_state.guessed_letters))

# 글자 입력

letter = st.text_input("추측할 글자를 입력하세요:", max_chars=1)

# 버튼 클릭 시 글자 추측 처리

if st.button("추측"):

    if letter:

        guess_letter(letter)

    else:

        st.warning("글자를 입력해주세요.")

# 게임 종료 확인

if st.session_state.attempts >= max_attempts:

    st.write("게임 오버! 정답은: ", secret_word)

    st.button("다시 시작", on_click=lambda: st.session_state.clear())

elif "_" not in st.session_state.display_word:

    st.write("축하합니다! 단어를 맞추셨습니다: ", secret_word)

    st.button("다시 시작", on_click=lambda: st.session_state.clear())