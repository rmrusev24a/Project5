import streamlit as st
import random

st.title("🔼 Higher or Lower 🔽")

# запазваме тайното число в сесията
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.tries = 0

st.write("Мисля си за число от 1 до 100")

guess = st.number_input(
    "Познай числото:",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Провери"):
    st.session_state.tries += 1

    if guess < st.session_state.secret:
        st.warning("⬆️ Higher (по-голямо)")
    elif guess > st.session_state.secret:
        st.warning("⬇️ Lower (по-малко)")
    else:
        st.success(f"🎉 Браво! Позна за {st.session_state.tries} опита")
        st.session_state.secret = random.randint(1, 100)
        st.session_state.tries = 0

if st.button("Нова игра"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.tries = 0
    st.info("Започна нова игра!")
