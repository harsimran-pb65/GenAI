import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt=PromptTemplate.from_template(
    "Answer the given question correctly and translate it in {language} language. \nQuestion: {question}"
)

llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.6)
chain= LLMChain(llm = llm, prompt=prompt)

st.title("Multilingual Q&A with Gemini")

language=st.selectbox(
    "Select the language for translation: ",
    ["hindi","Punjabi","French","German","Spanish","Chinese","Arabic"]
)

user_question=st.text_input("Ask a question: ")
if user_question: 
    result=chain.invoke({'language': language, 'question': user_question})
    st.subheader("Answer")
    st.write(result['text'])