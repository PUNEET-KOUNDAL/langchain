from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="google/gemma-2-2b-it",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm =llm)

result = model.invoke("what is the captial of india")


print(result)

# this is heavy process model need to download and then inference will be done