from typing import List, Union

from langchain_core.documents import Document
from src.lib.embedding_model import getEmbedding
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import JSONLoader

def processFile(file_type : str , file_path : str = None):
    """
    Processes a file based on the given file type and file path, returning a list of documents.
    
    Parameters:
        file_type (str): The type of the file to be processed.
        file_path (str, optional): The path to the file to be processed. Defaults to None.
        
    Returns:
        List[Document]: A list of documents extracted from the file.
    """
    embeddings = getEmbedding()

    documents : List[Document]
    if file_type == 'pdf':
        documents = get_documents_pdf(file_path)
    elif file_type == Union('txt', 'text'):
        documents  = get_documents_txt(file_path)
    elif file_type in Union('png', 'jpg', 'jpeg') :
        documents  = get_documents_img(file_path)
    elif file_type in Union('doc', 'docx') :
        documents  = get_documents_doc(file_path)
    elif file_type == 'json':
        documents  = get_documents_json(file_path)
    elif file_type == 'csv':
        documents  = get_documents_csv(file_path)
    else :
        raise ValueError('File type not supported')
    
    return documents

def get_documents_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()  
def get_documents_txt(file_path):
    loader = TextLoader(file_path)
    return loader.load()
def get_documents_img(file_path):
    pass
def get_documents_doc(file_path):
    pass
def get_documents_json(file_path):
    loader = JSONLoader(file_path)
    return loader.load()
def get_documents_csv(file_path):
    loader = CSVLoader(file_path)
    return loader.load()

