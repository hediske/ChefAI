

import os
from lib.chroma_database import getChromaDB, getChromaDBOnCloud
from lib.chroma_store import ChromaStore
from upload.lib.utils import prepareFile
from upload.lib.split_document import splitDocuments




def producer(filename,file_type,queue):
    docs = prepareFile(file_path=filename, file_type=file_type)
    print(f"Added the file '{filename}' to the queue")
    queue.put((docs,filename))


    
def consummer(queue,to_cloud = False):
    if to_cloud:
        chroma_client = ChromaStore(getChromaDBOnCloud())
    else:
        chroma_client = ChromaStore(getChromaDB())
    print(f"Process Nbr {os.getpid()} started working")
    while True:
        batch = queue.get()
        chroma_client.add_documents(batch[0])
        print(f" Process Nbr '{os.getpid()}' successfully added the file '{batch[1]}' to the vectorstore")
