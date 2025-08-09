


from lib.chroma_store import ChromaStore
from lib.chroma_database import getChromaDB




def getRetriever(component_type: str = "instructions", k: int = 3):
    """component_type: 'metadata', 'ingredients', or 'instructions'"""
    return ChromaStore(getChromaDB()).vectorstore.as_retriever(
        search_kwargs={
            "filter": {"chunk_type": component_type},
            "k": k
        }
    )