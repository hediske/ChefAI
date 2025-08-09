from concurrent.futures import ThreadPoolExecutor
from upload.lib.utils import get_files_from_folder
from upload.queue.queue_manager import QueueManager
from upload.queue.utils import producer
from upload.queue.consummer_pool import start_consummer_pool, stop_consummer_pool
import time

started = False



def start_uploading(queue = QueueManager().get_queue() ,num_consumers=8 ,to_cloud = False):
    start_consummer_pool(queue=queue , num_consumers=num_consumers ,to_cloud=to_cloud)
    global started
    started = True

def end_uploading():
    global started 
    stop_consummer_pool()
    started = False


def import_file(file_path,file_type:str= "recipe"):

    start_uploading(num_consumers=8)
    time.sleep(10)  # Give consumers time to start
    

    try:
        queue = QueueManager().get_queue()
        producer(file_path,file_type,queue)
        print(f"file {file_path} has been added to the queue")
    except Exception as e :
        print(f"Error importing file {file_path}: {e}")



def import_batch(folder_path,type:str= "recipe"):
    
    start_uploading(num_consumers=8)
    time.sleep(10) 
    if not started:
        print("Upload process not started.")
        return
    try:
        file_paths = get_files_from_folder(folder_path=folder_path)
        queue = QueueManager().get_queue()
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures =  [executor.submit(producer, file_path, type , queue) for file_path in file_paths]
            for future in futures:
                future.result()
        
        print(f"All files from folder {folder_path} have been added to the queue.")
    except Exception as e :
        print(f"Error importing files from folder {folder_path}: {e}")
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Path to single JSON file")
    parser.add_argument("--folder", help="Path to folder containing JSONs")
    parser.add_argument("--type", default="recipe", help="Type of the file(s) to import")
    parser.add_argument("--start", action="store_true", help="Start uploading process")
    parser.add_argument("--end", action="store_true", help="End uploading process")
    parser.add_argument("--to-cloud", action="store_true", help="Upload to cloud storage")
    parser.add_argument("--num-consumers", type=int, default=8, help="Number of consumer threads")
    args = parser.parse_args()

    if args.start:
        start_uploading(num_consumers=args.num_consumers, to_cloud=args.to_cloud)
        print("Started uploading process.")
    elif args.end:
        end_uploading()
        print("Ended uploading process.")
    elif args.file:
        import_file(args.file, file_type=args.type)
    elif args.folder:
        import_batch(args.folder)
    else:
        print("Please specify --start, --end, --file or --folder")