from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-haiku")

print(model.invoke("What is AI?").content)