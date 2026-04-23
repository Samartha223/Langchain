from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-pro")

response = model.invoke("Explain deep learning")
print(response.content)