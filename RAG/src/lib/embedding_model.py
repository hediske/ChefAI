from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY

def getEmbedding (api_key = OPENAI_API_KEY):
    embeddings =  OpenAIEmbeddings(openai_api_key = api_key)
    return embeddings