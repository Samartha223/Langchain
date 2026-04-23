from langchain_community.chat_models import ChatOllama

model = ChatOllama(model="tinyllama")

response = model.invoke("What is machine learning?")
print(response.content)