from langchain_core.runnables.history import RunnableWithMessageHistory

from src.lib.history_store import get_sessionStore
from src.lib.history_chain import getHistoryChain

def getHistoryConversionalChain():
    conversational_rag_chain = RunnableWithMessageHistory(
        getHistoryChain(),
        get_sessionStore,
        input_messages_key="input",
        history_messages_key="context",
        output_messages_key="answer",
        )
    return conversational_rag_chain