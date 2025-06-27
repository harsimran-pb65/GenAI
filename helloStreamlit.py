import streamlit as st

st.title("Hello, Streamlit!")
st.header("Welcome to your first Streamlit app.")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! 👋 Welcome to Streamlit.")
else:
    st.write("Please enter your name above.")