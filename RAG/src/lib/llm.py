from langchain_openai import ChatOpenAI
from config import HF_API_KEY, OPENAI_API_KEY
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


# def get_llm(api_key = OPENAI_API_KEY,  temperature = 0.1 , model = "gpt-3.5-turbo" , max_tokens = 512):
#     llm = ChatOpenAI(
#         openai_api_key = api_key,
#         temperature=temperature,
#         max_tokens=max_tokens,
#         model= model
#         )
#     return llm




def get_llm(api_key = HF_API_KEY,  temperature = 0.1 , model = "phamhai/Llama-3.2-3B-Instruct-Frog" , max_tokens = 512) :
    llm = HuggingFaceEndpoint(
        huggingfacehub_api_token=api_key,
        repo_id= model,
        temperature=temperature,
        task="text-generation",
        max_new_tokens=max_tokens,
        do_sample=False)
    
    return ChatHuggingFace(llm=llm)