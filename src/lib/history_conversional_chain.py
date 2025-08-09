from langchain_core.runnables.history import RunnableWithMessageHistory

from lib.chain import get_chain
from lib.history_store import get_sessionStore

def getHistoryConversionalChain():
    conversational_rag_chain = RunnableWithMessageHistory(
        get_chain(),
        get_sessionStore,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
        )
    return conversational_rag_chain