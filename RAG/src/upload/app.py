from concurrent.futures import ThreadPoolExecutor
from upload.lib.utils import get_files_from_folder
from upload.queue.queue_manager import QueueManager
from upload.queue.utils import producer
from upload.queue.consummer_pool import start_consummer_pool, stop_consummer_pool


started = False

def start_uploading(queue = QueueManager().get_queue() ,num_consumers=8 ,to_cloud = False):
    start_consummer_pool(queue=queue , num_consumers=num_consumers ,to_cloud=to_cloud)
    global started
    started = True

def end_uploading():
    global started 
    stop_consummer_pool()
    started = False


def import_file(file_path,file_type:str= None):
    try:
        queue = QueueManager().get_queue()
        producer(file_path,file_type,queue)
        print(f"file {file_path} has been added to the queue")
    except Exception as e :
        print(f"Error importing file {file_path}: {e}")



def import_batch(folder_path):
    try:
        file_paths = get_files_from_folder(folder_path=folder_path)
        queue = QueueManager().get_queue()
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures =  [executor.submit(producer, file_path, None , queue) for file_path in file_paths]
            for future in futures:
                future.result()
        
        print(f"All files from folder {folder_path} have been added to the queue.")
    except Exception as e :
        print(f"Error importing files from folder {folder_path}: {e}")