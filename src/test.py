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
import asyncio

def test_chroma_db():
    db = getChromaDB()
    print(db.list_collections())

def test_embeddings():
    embeddings = getEmbedding()
    query_result = embeddings.embed_query('hi im good thanks')
    print(query_result)

def test_llm():
    llm = get_llm()
    res = llm.invoke('what is the capital of Tunisia?')
    print(res)

def test_chain():
    chain = get_chain()
    question1 = "What is the paper about?"
    try:
        print({'input': question1})
        result = chain.invoke({'input': question1})
        print(result.get("answer"))
    except Exception as error:  
        print(error)

async def test_history_chain():
    all_chain = getHistoryConversionalChain()
    try:
        res = all_chain.invoke(
            {"input": "What is the capital of Tunis?"},
            {'configurable': {'session_id': 'testing'}}
        )["answer"]
        print(res)
        printStore()
        res2 = all_chain.invoke(
            {"input": "When was it built?"},
            {'configurable': {'session_id': 'testing'}}
        )["answer"]
        print(res2)
    except Exception as error:
        print(error)

def test_upload():
    start_uploading(num_consumers=4)
    time.sleep(5)  # Give consumers time to start
    import_file(file_path=r"C:\Users\moham\OneDrive\Documents\proj\RAG\Prepare_Hack\data\test.json")
    time.sleep(10)  # Give time for processing

if __name__ == '__main__':
    # Uncomment the tests you want to run
    # test_chroma_db()
    # test_embeddings()
    # test_llm()
    # test_chain()
    # asyncio.run(test_history_chain())
    test_upload()