from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model="gpt-4")

response= model.invoke("what is the capital of India?") #takes in string as an input and returns a output with metadata 

print(response.content)