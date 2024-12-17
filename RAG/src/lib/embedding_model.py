from langchain_openai.embeddings import OpenAIEmbeddings
from src.config import OPENAI_API_KEY

def getEmbedding (api_key = OPENAI_API_KEY):
    embeddings =  OpenAIEmbeddings(model='text-embedding-ada-002',openai_api_key = api_key)
    return embeddings