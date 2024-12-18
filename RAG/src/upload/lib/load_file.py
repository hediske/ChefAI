from typing import List, Union

from langchain_core.documents import Document
from lib.embedding_model import getEmbedding
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
    """
    Loads and extracts documents from a PDF file.

    Parameters:
        file_path (str): The path to the PDF file.

    Returns:
        Document: The extracted document.
    """
    loader = PyPDFLoader(file_path)
    return loader.load()  
def get_documents_txt(file_path):
    """
    Loads and extracts documents from a text file.

    Parameters:
        file_path (str): The path to the text file.

    Returns:
        Document: The extracted document.
    """
    loader = TextLoader(file_path)
    return loader.load()
def get_documents_img(file_path):
    """
    Loads and extracts documents from an image file.

    Parameters:
        file_path (str): The path to the image file.

    Returns:
        Document: The extracted document.
    """
    pass
def get_documents_doc(file_path):
    pass
def get_documents_json(file_path):
    """
    Loads and extracts documents from a JSON file.

    Parameters:
        file_path (str): The path to the JSON file.

    Returns:
        Document: The extracted document.
    """
    loader = JSONLoader(file_path)
    return loader.load()
def get_documents_csv(file_path):
    """
    Loads and extracts documents from a CSV file.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        Document: The extracted document.
    """
    loader = CSVLoader(file_path)
    return loader.load()

