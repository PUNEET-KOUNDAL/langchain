from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI = OpenAI(model ='gpt-4' , temperature=  0.5 , max_tokens= 100)

result = model.invoke("what is the captial of delhi")

print(result)

print(result.content)
