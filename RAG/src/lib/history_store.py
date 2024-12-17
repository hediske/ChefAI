from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory



store = {}


def get_historyStore():
    return store


def get_sessionStore(session_id :str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def initialize_session(session_id):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    else:
        store[session_id].clear()