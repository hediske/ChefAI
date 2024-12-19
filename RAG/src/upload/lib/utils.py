

import os
from lib.chroma_database import getChromaDB, getChromaDBOnCloud
from lib.chroma_store import ChromaStore
from upload.lib.generate_docs import processFile

def get_file_type(file_path: str , file_type : str = None):
    return  file_type if file_type else file_path.split('.')[-1]

def get_files_from_folder(folder_path: str ):
    """
    Generates a list of file paths within a specified folder.

    Parameters:
        folder_path (str): The path to the folder.
        file_type (str, optional): The type of files to filter. Defaults to None.

    Returns:
        List[str]: A list of file paths within the folder.
    """
    return [os.path.join(folder_path, f)
             for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f))]



def prepareFile(file_path: str , file_type : str = None):
    """
    A function that prepares a file for processing based on the file path and type.

    Parameters:
    file_path (str): The path to the file.
    file_type (str, optional): The type of the file. If not provided, it is inferred from the file path.

    Returns:
    The result of processing the file as a list of documents.
    """
    file_type = get_file_type(file_path=file_path,file_type=file_type)
    return processFile(file_type=file_type,file_path=file_path)
