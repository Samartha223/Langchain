from langchain_ollama import ChatOllama
from pydantic import BaseModel,Field
from typing import Optional


model = ChatOllama(model='tinyllama')

class Review(BaseModel):
    summary:str =Field(...,description="A brief summary of the review")
    sentiment:str =Field(...,description="The overall sentiment of the review, either 'pos', 'neg', or 'neu'")
    score:Optional[float] =Field(None,description="An optional score from 0 to 1 indicating the strength of the sentiment")

review = "Great travel insurance – Great travel insurance cheap easy to apply for no problems I have used them twice an will definitely use them again"
structured_model = model.with_structured_output(Review)

response = structured_model.invoke(review)
print(response)



