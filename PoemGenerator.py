import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAVdOnE9qyK0gpJwt1KXIg-TIPE9zFn--w")

model=genai.GenerativeModel("gemini-2.0-flash")

st.title("Simple Poem Generator")

user_input=st.text_input("Enter a word or sentence for your poem: ")

if st.button("Generate Poem") and user_input:
    response=model.generate_content(f"Write a poem about: {user_input}")
    poem=response.text
    st.subheader("Your Poem: ")
    st.write(poem)

    st.session_state['poem']=poem

st.subheader("Transform your poem")
if 'poem' in st.session_state:
    choice=st.selectbox("", 
                        ["Shorten the poem",
                         "Expand the poem",
                         "Rewrite the poem in a different style",
                         "Change the tone of the poem"
                        ],
                        index=None,
                        placeholder="Choose an option")
    extra=""

    if choice=="Rewrite the poem in a different style":
        extra = st.text_input("Enter style (e.g., haiku, rap, old English): ")
    elif choice=="Change the tone of the poem":
        extra= st.text_input("Enter tone(e.g., joyful, sad, funny): ")
    
    if st.button("Transform Poem") and choice:
        prompt=" "
        if choice=="Shorten the poem":
            prompt=f"shorten this poem:\n {st.session_state['poem']}"
        elif choice=="Expand the poem":
            prompt=f"Expand this poem with more detail:\n {st.session_state['poem']}"
        elif choice=="Rewrite the poem in different style":
            prompt=f"Rewrite this poem in {extra}:\n {st.session_state['poem']}"
        elif choice=="Change the tone of the poem":
            prompt=f"Change the tone of this poem to {extra}:\n {st.session_state['poem']}"

        response=model.generate_content(prompt)
        new_poem=response.text

        st.subheader("Transformed Poem:")
        st.write(new_poem)

else: 
    st.info("Generate a poem first to transform it.")
