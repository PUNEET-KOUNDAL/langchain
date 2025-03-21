from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  


load_dotenv()

model = ChatGoogleGenerativeAI(model ='gemini-1.5-pro', temperature=  0.5 , max_tokens= 70)

result = model.invoke("tell me about your self")

print(result.content)