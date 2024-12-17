from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder


HISTORY_RETRIEVAL_TEMPLATE = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)


def getHistoryTemplate():
    return HISTORY_RETRIEVAL_TEMPLATE

def getHistoryPrompt() -> ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages([
        ("system", getHistoryTemplate()),
        MessagesPlaceholder("context"),
        ("human", "{input}"),
    ])
    return prompt
