import chromadb


from src.config import CHROMADB_DIRECTORY ,CHROMADB_CLOUD_DATABASE,CHROMADB_CLOUD_HOST,CHROMADB_CLOUD_PORT

def getChromaDB(InMemroy: bool = False):
    return chromadb.Client(
        settings={"local": {"data_dir": CHROMADB_DIRECTORY}}
    ) if InMemroy else chromadb.Client()


def getChromaDBOnCloud(database = CHROMADB_CLOUD_DATABASE ,host : str = CHROMADB_CLOUD_HOST , port : int = CHROMADB_CLOUD_PORT , ssl : bool = False  ): 
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=ssl,
        database=database
    )