from threading import Lock
from langchain_chroma import Chroma
from typing import List
from langchain_core.documents import Document
from lib.embedding_model import getEmbedding


class ChromaStore:
    _instance = None
    _lock = Lock()  # Lock to ensure the thread safety (using the Pool of Consummers)
    _initialized = False

    
    def __new__(cls, client: Chroma = None):
        with cls._lock:
            if cls._instance is None:
                if client is None:
                    raise ValueError("Client must be provided for the first initialization.")
                cls._instance = super(ChromaStore, cls).__new__(cls)
                cls._instance._initialize(client)
            elif not cls._initialized and client is not None:
                cls._instance._initialize(client)
        return cls._instance

    def _initialize(self, client: Chroma):
        self.vectorstore = Chroma(
            client=client,
            embedding_function=getEmbedding(),
        )
        self.__class__._initialized = True

    def add_documents(self, docs: List[Document]):
        if not hasattr(self, "vectorstore"):
            raise RuntimeError("ChromaStore is not initialized. Ensure it is created with a client.")
        self.vectorstore.add_documents(docs)
        print(f"uccessfully Added {len(docs)} documents to the vectorstore")


    def is_initialized(self):
        return hasattr(self, "vectorstore") and self.__class__._initialized
    

    @classmethod
    def reset_instance(cls):
        with cls._lock:
            cls._instance = None
            cls._initialized = False
        print("ChromaStore has been reset.")