from langchain_community.llms import Ollama

llm= Ollama(model="tinyllama")

print(llm.invoke("What is the capital of India?"))