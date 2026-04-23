from langchain_ollama import ChatOllama
import streamlit as st #for the UI
from langchain_core.prompts import PromptTemplate

st.title("Dynamic prompt example")

model = ChatOllama(model='mistral')

user_input = st.text_area("Enter the text of the research paper:")

template = PromptTemplate(template="""
You are a helpful AI specialized in analyzing research papers.

Summarize the following paper:

{text}

Return the output in this format:

1. Title (if available)
2. Objective
3. Methodology
4. Key Findings
5. Conclusion

Keep it simple and easy to understand.
""",input_variable=['text'])

prompt = template.invoke({"text": user_input})

if st.button("Summarize"):
    response = model.invoke(prompt)

    st.write(response.content)

    print(response.content)

