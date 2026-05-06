from langchain_ollama import ChatOllama
from typing import TypedDict,Annotated

model = ChatOllama(model='tinyllama')

class Review(TypedDict):
    summary:Annotated[str, "A brief summary of the review"]
    sentiment:Annotated[str, "The overall sentiment of the review, either 'pos', 'neg', or 'neu'"]

review = "Great travel insurance – Great travel insurance cheap easy to apply for no problems I have used them twice an will definitely use them again"

structured_model = model.with_structured_output(Review)

response = structured_model.invoke(review)
print(response)