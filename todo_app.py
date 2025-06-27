import streamlit as st
st.title("To-Do list")
if "tasks" not in st.session_state:
    st.session_state.tasks=[]
new_task=st.text_input("Add a new task")
if st.button("Add task"):
    st.session_state.tasks.append(new_task)
    st.success("Task added!")
st.subheader("Your tasks: ")
for t in st.session_state.tasks:
    st.write("-", t)
