
from src.lib.chroma_database import getChromaDB
from src.lib.embedding_model import getEmbedding
from src.lib.llm import get_llm
from src.lib.chroma_retriever import getRetriever
from src.upload.lib.import_file import import_file
from src.upload.lib.split_document import splitDocuments
from src.lib.chain import get_chain

# print("trying the app")
# import_file(file_path = r"c:\Users\moham\Downloads\Exercies\Prepare_Hack\RAG\data\load\Metamorphosis.pdf",file_type="pdf")


chain = get_chain()
# llm = get_llm()
retriever = getRetriever()
print(chain)
chain.invoke({'input' : "What is the paper about?"})

