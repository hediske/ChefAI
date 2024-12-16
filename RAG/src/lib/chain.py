
from Prepare_Hack.RAG.src.lib.chromaRetriever import getRetriver
from Prepare_Hack.RAG.src.lib.llm import get_llm
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from Prepare_Hack.RAG.src.lib.prompt import getPrompt

def get_chain() :
    llm = get_llm()
    combine_docs_chain = create_stuff_documents_chain(llm, getPrompt())
    retrieval_chain = create_retrieval_chain(
        retriever=getRetriver(),
        combine_documents_chain=combine_docs_chain,
        return_source_documents=True )
    return retrieval_chain
