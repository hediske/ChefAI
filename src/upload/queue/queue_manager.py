
import  multiprocessing as mp


class QueueManager:
    _instance = None
    _queue : mp.Queue = None


    def __new__(cls):
        if not cls._instance:
            cls._instance = super(QueueManager, cls).__new__(cls)
            cls._queue = mp.Queue()
        return cls._instance

    def get_queue(self) -> mp.Queue:
        return self._queue
