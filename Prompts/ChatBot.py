from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage


model = ChatOllama(model='mistral')

chat_history =[SystemMessage("You are a helpful assistant.")]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print("Chatbot:",response.content)
print("Chat history:", chat_history)