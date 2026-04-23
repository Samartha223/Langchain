#Using the ollama chat models to answer the questions

from langchain_community.chat_models import ChatOllama

chat = ChatOllama(model="tinyllama")

response = chat.invoke("Who is the president of the Russia?")
print(response)