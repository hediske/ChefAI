from langchain_chroma import Chroma
from typing import List
from langchain_core.documents import Document
from src.lib.embedding_model import getEmbedding


class ChromaStore:
    _instance = None

    def __new__(cls, client: Chroma = None):
        if cls._instance is None:
            if client is None:
                raise ValueError("Client must be provided for the first initialization.")
            cls._instance = super(ChromaStore, cls).__new__(cls)
            cls._instance._initialize(client)
        return cls._instance

    def _initialize(self, client: Chroma):
        self.vectorstore = Chroma(
            client=client,
            embedding_function=getEmbedding(),
        )
        print("Initialized Vectorstore")

    def add_documents(self, docs: List[Document]):
        if not hasattr(self, "vectorstore"):
            raise RuntimeError("ChromaStore is not initialized. Ensure it is created with a client.")
        self.vectorstore.add_documents(docs)
        print(f"Added {len(docs)} documents to the vectorstore")