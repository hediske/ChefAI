
from src.lib.evoke_RAG import evoke_and_save
from src.lib.history_store import get_sessionStore, printStore
from src.lib.chroma_store import ChromaStore
from src.lib.history_conversional_chain import getHistoryConversionalChain
from src.lib.history_retriever import getHistoryRetriever
from src.lib.chroma_database import getChromaDB
from src.lib.embedding_model import getEmbedding
from src.lib.llm import get_llm
from src.lib.chroma_retriever import getRetriever
from src.upload.lib.import_file import import_file
from src.upload.lib.split_document import splitDocuments
from src.lib.chain import get_chain



# Testing the Chroma Db
# db = getChromaDB()
# print(db.list_collections())


# Testing the embeddings
# embeddings = getEmbedding()
# query_result = embeddings.embed_query('hi im good thanks')
# print (query_result)


# Testing the LLM
# llm = get_llm()
# res=llm.invoke('what is the capital of Tunisia ? ')
# print(res)


#Testing the import
# print("Trying the app")
# print("Uploading a file to the local database")
# import_file(file_path = r"c:\Users\moham\Downloads\Exercies\Prepare_Hack\RAG\data\load\Metamorphosis.pdf",file_type="pdf")




#Testing the Chain
# chain = get_chain()
# question1 = "What is the paper about?"
# try:
#     print ({'input' : question1})
#     result = chain.invoke({'input' : question1})
#     print(result.get("answer"))
# except Exception as error:  
#     print(error)




# #Testing the History Chain with the store
# all_chain = getHistoryConversionalChain()
# try:
#     res = all_chain.invoke(
#     {"input": "What is the capital of Tunis ? "},
#     {'configurable': {'session_id': 'testing'}}
#     )["answer"]
#     print(res)
#     printStore()
#     res2 = all_chain.invoke(
#     {"input": "When was it built ?"},
#     {'configurable': {'session_id': 'testing'}}
#     )["answer"]
#     print(res2)
# except Exception as error:
#     print(error)


res = evoke_and_save("test", "What is the paper about ?")
print(res)

res2 = evoke_and_save("test", "suggest other papers similar ?")
print(res2)