import chromadb


from config import CHROMADB_DIRECTORY

def getChromaDB(InMemroy: bool = False):
    return chromadb.Client(
        settings={"local": {"data_dir": CHROMADB_DIRECTORY}}
    ) if InMemroy else chromadb.Client()


def getChromaDBOnCloud(host : str = "localhost", port : int = 8000 , ssl : bool = False): 
    return chromadb.HttpClient(
        host=host,
        port=port,
        ssl=ssl,
    )