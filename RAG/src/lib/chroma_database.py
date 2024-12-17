import chromadb


from src.config import CHROMADB_DIRECTORY ,CHROMADB_CLOUD_DATABASE,CHROMADB_CLOUD_HOST,CHROMADB_CLOUD_PORT

def getChromaDB(path: str = CHROMADB_DIRECTORY):
    return chromadb.PersistentClient(path=path)


def getChromaDBOnCloud(database = CHROMADB_CLOUD_DATABASE ,host : str = CHROMADB_CLOUD_HOST , port : int = CHROMADB_CLOUD_PORT , ssl : bool = False  ): 
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=ssl,
        database=database
    )