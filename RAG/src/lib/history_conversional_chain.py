from langchain_core.runnables.history import RunnableWithMessageHistory

from src.lib.chain import get_chain
from src.lib.history_store import get_sessionStore

def getHistoryConversionalChain():
    conversational_rag_chain = RunnableWithMessageHistory(
        get_chain(),
        get_sessionStore,
        input_messages_key="input",
        history_messages_key="history",
        output_messages_key="answer",
        )
    return conversational_rag_chain