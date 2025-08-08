
import time
from upload.queue.utils import producer
from upload.app import import_batch, import_file, start_uploading
from lib.evoke_RAG import evoke_and_save
from lib.history_store import get_sessionStore, printStore
from lib.chroma_store import ChromaStore
from lib.history_conversional_chain import getHistoryConversionalChain
from lib.history_retriever import getHistoryRetriever
from lib.chroma_database import getChromaDB
from lib.embedding_model import getEmbedding
from lib.llm import get_llm
from lib.chroma_retriever import getRetriever
from upload.lib.split_document import splitDocuments
from lib.chain import get_chain



# Testing the Chroma Db
# db = getChromaDB()
# print(db.list_collections())


# Testing the embeddings
embeddings = getEmbedding()
query_result = embeddings.encode('hi im good thanks')
print (query_result)


# Testing the LLM
llm = get_llm()
res=llm.invoke('what is the capital of Tunisia ? ')
print(res)


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




# # #Testing the History Chain with the store
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


# res = asyncio.run(evoke_and_save("test", "What is the paper about ?"))
# print(res)

# res2 = asyncio.run(evoke_and_save("test", "suggest other papers similar ?"))
# print(res2)




# if __name__ == '__main__':

#     start_uploading(num_consumers=4)
#     time.sleep(20)
#     import_batch(r"c:\Users\moham\Downloads\Exercies\Prepare_Hack\RAG\data\load\Stories")
#     # import_file(r"c:\Users\moham\Downloads\Exercies\Prepare_Hack\RAG\data\load\Metamorphosis.pdf",file_type="pdf")
