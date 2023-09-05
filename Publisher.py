import threading
from queue import Queue


class Publisher(threading.Thread):

    def __init__(self, queue: Queue, sentinel):
        threading.Thread.__init__(self)
        self.thread_name = "Publisher"
        self._delay = 2
        self._queue = queue
        self._sentinel = sentinel

    def add(self, animal: str):
        self._queue.put(animal)
        print(f"Animal Sighted: {animal}")

    def add_sentinel(self):
        self._queue.put(self._sentinel)
