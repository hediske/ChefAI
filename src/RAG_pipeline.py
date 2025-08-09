from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import  create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


from lib.llm import get_llm
from lib.chroma_retriever import getRetriever


retriever = getRetriever()
model=get_llm()

# --- 2. Prompt for retriever reformulation ---
retriever_prompt = (
    "Given a chat history and the latest user question which might reference "
    "context in the chat history, formulate a standalone question which can be "
    "understood without the chat history. Do NOT answer the question."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", retriever_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

# --- 3. History-aware retriever ---
history_aware_retriever = create_history_aware_retriever(model, retriever, contextualize_q_prompt)

# --- 4. Main QA prompt with context ---
system_prompt = (
    "You are ChefAI, a culinary expert assistant. "
    "Use the retrieved context to answer. "
    "If you don't know, say so. Be concise.\n\n{context}"
)

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

# --- 5. Document chain ---
question_answer_chain = create_stuff_documents_chain(model, qa_prompt)

# --- 6. Retrieval + QA ---
rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

# --- 7. Store for session history ---
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# --- 8. Wrap chain with message history ---
conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

# --- 9. Example usage ---
response1 = conversational_rag_chain.invoke(
    {"input": "Show me recipe with chicken and oil"},
    config={"configurable": {"session_id": "chef123"}}
)
print(response1["answer"])

response2 = conversational_rag_chain.invoke(
    {"input": "Can you give me instructions"},
    config={"configurable": {"session_id": "chef123"}}
)
print(response2["answer"])
