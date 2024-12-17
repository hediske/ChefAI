from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from src.lib.history_prompt import getHistoryPrompt
from src.lib.history_retriever import getHistoryRetriever
from src.lib.llm import get_llm


def getHistoryChain():
    combine_hist_chain = create_stuff_documents_chain(get_llm(), getHistoryPrompt())
    return create_retrieval_chain(getHistoryRetriever(), combine_hist_chain )