import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyAVdOnE9qyK0gpJwt1KXIg-TIPE9zFn--w")

model=genai.GenerativeModel("gemini-1.5-flash")

st.title("Ask anything from Gemini AI")

question=st.text_input("Enter your question: ")
if question:
    with st.spinner("Generating..."):
        response=model.generate_content(question)
        st.subheader("Answer: ")
        st.write(response.text)
