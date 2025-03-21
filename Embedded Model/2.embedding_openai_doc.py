from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model ='ext-embedding-3-large', dimesion = 32 )

document = [


    "Delhi is the capital of India",
    "India is a country in South Asia",
    "India is known for its diverse culture",
    "India has a population of over 1.3 billion people",   
]


result = embeddings.embed_document(document)

print(str(result))  #show vector