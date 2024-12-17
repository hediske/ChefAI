
from openai import RateLimitError
from src.lib.history_conversional_chain import getHistoryConversionalChain
from src.lib.history_retriever import getHistoryRetriever
from src.lib.history_chain import getHistoryChain
from src.lib.chroma_database import getChromaDB
from src.lib.embedding_model import getEmbedding
from src.lib.llm import get_llm
from src.lib.chroma_retriever import getRetriever
from src.upload.lib.import_file import import_file
from src.upload.lib.split_document import splitDocuments
from src.lib.chain import get_chain


#Testing the import

# print("trying the app")
# import_file(file_path = r"c:\Users\moham\Downloads\Exercies\Prepare_Hack\RAG\data\load\Metamorphosis.pdf",file_type="pdf")


#Testing the Chain
# chain = get_chain()
# question1 = "What is the paper about?"
# try:
#     result = chain.invoke({'input' : question1})
# except RateLimitError as error:  
#     print(error)


#Testing the History Chain 
# from langchain_core.messages import  HumanMessage
# from langchain_core.messages import  AIMessage
# history_data =[]
# question2 = "What is the task decomposition?"
# question3 = "What are the examples of that ?"
# history_chain = getHistoryChain()
# try:
#     aiMsg = history_chain.invoke({'input' : "What is the task decomposition?" , "context" : history_data})
#     history_data = [
#         HumanMessage(content=question2)
#         ,AIMessage(content=aiMsg["answer"])
#     ]
#     ai_msg_2 = history_chain.invoke({"input": question3, "chat_history": history_data})
#     print(ai_msg_2["answer"])
# except RateLimitError as error:
#     print(error)



#Testing the History Chain with the store
all_chain = getHistoryConversionalChain()
try:
    all_chain.invoke(
    {"input": "What is the task decomposition?"},
    {'configurable': {'session_id': '123'}}
    )["answer"]
except RateLimitError as error:
    print(error)