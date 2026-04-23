from langchain_community.chat_models import ChatOllama
import streamlit as st #for the UI

st.title("Static prompt example")

model = ChatOllama(model='tinyllama')

# static prompt (hardcoded)
user_input = st.text_input("Enter your question:")

if  st.button("Submit"):
    response = model.invoke(user_input)

    st.write(response.content)

#When to use
"""
Testing models
Simple one-time queries
Fixed instructions"""
