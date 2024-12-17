

from src.lib.chroma_database import getChromaDB, getChromaDBOnCloud
from src.lib.chroma_store import ChromaStore
from src.upload.lib.load_file import processFile


def prepareFile(file_path: str , file_type : str = None):
    file_type = file_type if file_type else file_path.split('.')[-1]
    return processFile(file_type=file_type,file_path=file_path)


def import_file(file_path: str , file_type : str = None):
    try:    
        chroma_store = ChromaStore(getChromaDB())
        docs =  prepareFile(file_type=file_type,file_path=file_path)
        chroma_store.add_documents(docs)
        print(f"Successfully imported file {file_path} into the local Chroma database.")
    except Exception as e:
        print(f"Failed to import file {file_path}: {e}")


def import_file_to_cloud(file_path: str,file_type : str = None):
    try:
        chroma_store = ChromaStore(getChromaDBOnCloud())
        docs =  prepareFile(file_path=file_path,file_type=file_type)
        chroma_store.add_documents(docs)
        print(f"Successfully imported file {file_path} into the cloud Chroma database.")
    except Exception as e:
        print(f"Failed to import file {file_path} to the cloud: {e}")

