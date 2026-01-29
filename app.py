import streamlit as st

st.title("Малка програма с въпрос")

name = st.text_input("Как се казваш?")
age = st.number_input(
    "На колко години си?",
    min_value=0,
    max_value=120,
    step=1
)

if st.button("Провери"):
    st.write("Здравей,", name)

    if age >= 18:
        st.success("Ти си пълнолетен.")
    else:
        st.warning("Ти не си пълнолетен.")
