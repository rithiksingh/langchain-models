from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    provider="together",        # specify the provider that hosts the model
    task="text-generation",     # optional, defaults match the repo’s config
    max_new_tokens=256,         # you can also tune generation params
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)