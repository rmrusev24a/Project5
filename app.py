import streamlit as st
import random

st.title("🎯 Познай числото")

# тайно число
secret = random.randint(1, 10)

st.write("Мисля си за число от 1 до 10")

guess = st.number_input(
    "Твоето предположение:",
    min_value=1,
    max_value=10,
    step=1
)

if st.button("Провери"):
    if guess == secret:
        st.success("Браво! Позна!")
    else:
        st.error("Не позна 😢 Опитай пак")
