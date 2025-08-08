


from lib.chroma_store import ChromaStore
from lib.chroma_database import getChromaDB



def getRetriever():
    chromastore = ChromaStore(getChromaDB())
    return chromastore.vectorstore.as_retriever()
