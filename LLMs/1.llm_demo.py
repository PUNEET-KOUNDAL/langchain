from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model ='gpt-3.5-turbo')
result = llm.invoke("what is the captial of delhi")
print(result)

#this is langchain older openai version support , even langchain doest support this approach
