import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai

genai.configure(api_key="AIzaSyAVdOnE9qyK0gpJwt1KXIg-TIPE9zFn--w")  
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("AI Resume Feedback App")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_resume_feedback(text):
    prompt = (
        "You are an expert resume reviewer. Analyze the following resume text. "
        "Point out any mistakes, grammar issues, or formatting errors. Also give suggestions to improve the resume. "
        "Here is the resume:\n\n"
        + text
    )
    response = model.generate_content(prompt)
    return response.text

if uploaded_file:
    with st.spinner("Extracting text from resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Generating AI feedback..."):
        feedback = get_resume_feedback(resume_text)

    st.subheader("AI Feedback and Suggestions:")
    st.markdown(feedback)