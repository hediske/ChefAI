from langchain.chains import create_history_aware_retriever

from src.lib.chroma_retriever import getRetriever
from src.lib.history_prompt import getHistoryPrompt
from src.lib.llm import get_llm


def getHistoryRetriever():
    return create_history_aware_retriever(
        llm = get_llm(),
        retriever=getRetriever(),
        prompt= getHistoryPrompt(),
    )