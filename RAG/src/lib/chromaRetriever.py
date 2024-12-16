from typing import List
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import BaseRetriever, Document
from langchain.callbacks.manager import (
    CallbackManagerForRetrieverRun,
    AsyncCallbackManagerForRetrieverRun,
)
from Prepare_Hack.RAG.src.lib.ChromaDb import getChromaDB

from pydantic import BaseModel

from Prepare_Hack.RAG.src.lib.llm import get_llm


class ChromaRetriever(BaseRetriever, BaseModel):
    top_k: int = 5  
    similarity_threshold: float = 0.7 
    embeddings: OpenAIEmbeddings
    chroma : Chroma

    def _get_relevant_documents(self, query: str, *, run_manager: CallbackManagerForRetrieverRun) -> List[Document]:
        
        query_embedding = self.embeddings.embed_query(query)
        similar_docs  = self.chroma.similarity_search_with_score(query_embedding, k=self.top_k)

        relevent_docs = [
                Document(page_content=doc.page_content, metadata = doc.metadata)
                for doc , score in similar_docs 
                if score >= self.similarity_threshold
        ]
        return relevent_docs
    



    async def _aget_relevant_documents(self, query: str, *, run_manager: AsyncCallbackManagerForRetrieverRun) -> List[Document]:
        return self._get_relevant_documents(query, run_manager=run_manager)




def getRetriver():
    return ChromaRetriever(
        top_k = 5,
        similarity_threshold = 0.7,
        embeddings = get_llm(),
        chroma = getChromaDB()
    )
