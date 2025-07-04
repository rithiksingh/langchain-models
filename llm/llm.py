# This is the class which have all the ope
from langchain_openai import OpenAI 
from dotenv import load_dotenv

load_dotenv()

llm= OpenAI(model='gpt-3.5-turbo-instruct')

result= llm.invoke("what is the capital of India") # takes in string as an input and gives string as an output
print("hey")
print(result)

