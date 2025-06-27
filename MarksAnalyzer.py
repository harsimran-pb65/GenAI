import streamlit as st
import pandas as pd

# Title of the App
st.title("Marks Analyzer App")

# Subject list
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = []

# Input fields for each subject
st.header("Enter Marks for Each Subject (Out of 100)")
for subject in subjects:
    mark = st.number_input(f"{subject} Marks:", min_value=0, max_value=100, step=1)
    marks.append(mark)

# Button to analyze marks
if st.button("Analyze"):
    total = sum(marks)
    average = total / len(marks)

    # Display total and average
    st.subheader("Results")
    st.write("Total Marks:", total)
    st.write("Average Marks:", round(average, 2))

    # Show bar chart
    df = pd.DataFrame({'Subject': subjects, 'Marks': marks})
    st.subheader("Marks Bar Chart")
    st.bar_chart(df.set_index('Subject'))

    # Feedback message
    st.subheader("Performance Feedback")
    if average >= 80:
        st.success("Excellent performance!")
    elif average >= 60:
        st.info("Good job!")
    else:
        st.warning("Needs Improvement. Keep practicing!")