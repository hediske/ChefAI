

from multiprocessing import Process

from upload.queue.utils import consummer


def start_consummer_pool(queue, num_consumers=8, to_cloud=False):
    pool = []
    for _ in range(num_consumers):
        process = Process(target=consummer, args=(queue, to_cloud))
        process.daemon = False
        process.start()
        pool.append(process)
    print(f"launched a Pool of Consummer with {len(pool)} process")
    return pool


def stop_consummer_pool(pool,queue):
    for _ in pool:
        queue.put(None)
    for process in pool:
        process.join()
