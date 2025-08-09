from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory



store = {}

def get_historyStore():
    return store


def get_sessionStore(session_id :str) -> BaseChatMessageHistory:
    key = session_id
    if key not in store:
        store[key] = ChatMessageHistory()
    return store[key]

def printStore():
    print(store)


def remove_sessionStore(session_id :str):
    key = session_id
    if key in store:
        del store[key]

