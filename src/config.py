import os
from dotenv import load_dotenv , find_dotenv

_ = load_dotenv(find_dotenv())

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

HF_API_KEY = os.getenv('HF_API_KEY')

CHROMADB_DIRECTORY = os.getenv('CHROMADB_DIRECTORY')
CHROMADB_CLOUD_HOST = os.getenv('CHROMADB_CLOUD_HOST')
CHROMADB_CLOUD_PORT = os.getenv('CHROMADB_CLOUD_PORT')
CHROMADB_CLOUD_DATABASE = os.getenv('CHROMADB_CLOUD_DATABASE')