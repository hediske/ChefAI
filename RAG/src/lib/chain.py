
from lib.history_retriever import getHistoryRetriever
from lib.chroma_retriever import getRetriever
from lib.llm import get_llm
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from lib.prompt import getPrompt

def get_chain() :
    llm = get_llm()
    combine_docs_chain = create_stuff_documents_chain(llm, getPrompt())
    retrieval_chain = create_retrieval_chain(
        # retriever= getRetriever(),
        retriever= getHistoryRetriever(),
        combine_docs_chain=combine_docs_chain )
    return retrieval_chain
