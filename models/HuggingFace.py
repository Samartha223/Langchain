from langchain_community.llms import HuggingFaceHub

model = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    huggingfacehub_api_token="YOUR_TOKEN"
)

print(model.invoke("Explain AI"))