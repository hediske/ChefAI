
from typing import List
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter as RCS


text_splitter = RCS.from_tiktoken_encoder(
            chunk_size = 300,
            chunk_overlap = 200
    )

def splitDocuments(docs : List[Document]):
    chunks = text_splitter.split_documents(docs)
    return chunks




def splitDocument(doc :Document):
    chunks = text_splitter.split_text(doc.page_content)
    return chunks

