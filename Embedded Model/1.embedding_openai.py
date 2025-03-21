from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model ='ext-embedding-3-large', dimesion = 32 )
result = embeddings.embed_query("delhi is the captia of india ")

print(str(result))  #show vector