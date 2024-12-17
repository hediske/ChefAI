


from src.lib.embedding_model import getEmbedding
from src.lib.chroma_store import ChromaStore
from src.lib.chroma_database import getChromaDB



def getRetriever():
    chromastore = ChromaStore(getChromaDB())
    print ("Retriever initialized")
    return chromastore.vectorstore.as_retriever()
