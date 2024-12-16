import os
from dotenv import load_dotenv , find_dotenv

_ = load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


CHROMADB_DIRECTORY = os.getenv('CHROMADB_DIRECTORY')
CHROMADB_CLOUD_DIRECTORY = os.getenv('CHROMADB_CLOUD_DIRECTORY') or CHROMADB_DIRECTORY