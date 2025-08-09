
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
        retriever= getHistoryRetriever(),
        combine_docs_chain=combine_docs_chain )

    return retrieval_chain

    # from langchain_core.runnables import RunnableLambda

    # retrieval_chain_with_logging = RunnableLambda(
    #     lambda x: retrieval_chain.invoke(x)
    # ).with_config(callbacks=[
    #     lambda doc: print("Retrieved documents:\n", doc)
    # ])
    # return retrieval_chain_with_logging
