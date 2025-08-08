from sentence_transformers import SentenceTransformer
from config import HF_API_KEY, OPENAI_API_KEY

# def getEmbedding (api_key = OPENAI_API_KEY):
#     embeddings =  OpenAIEmbeddings(model='text-embedding-ada-002',openai_api_key = api_key)
#     return embeddings




def getEmbedding (api_key = HF_API_KEY,model_name = "intfloat/multilingual-e5-large"):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model
