


from lib.embedding_model import getEmbedding
from lib.chroma_store import ChromaStore
from lib.chroma_database import getChromaDB



def getRetriever():
    chromastore = ChromaStore(getChromaDB())
    print ("Retriever initialized")
    return chromastore.vectorstore.as_retriever()
