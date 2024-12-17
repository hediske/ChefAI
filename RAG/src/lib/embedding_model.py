from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from src.config import HF_API_KEY, OPENAI_API_KEY

# def getEmbedding (api_key = OPENAI_API_KEY):
#     embeddings =  OpenAIEmbeddings(model='text-embedding-ada-002',openai_api_key = api_key)
#     return embeddings



def getEmbedding (api_key = HF_API_KEY,model = "sentence-transformers/all-mpnet-base-v2"):
    embeddings =  HuggingFaceInferenceAPIEmbeddings (
        model_name=model,
        api_key = api_key)
    return embeddings