import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, element: int) -> None:
        with self.lock:
            while len(self.queue) == self.capacity:
                self.not_full.wait()
            self.queue.append(element)
            self.not_empty.notify()

    def dequeue(self) -> int:
        with self.lock:
            while len(self.queue) == 0:
                self.not_empty.wait()
            element = self.queue.pop(0)
            self.not_full.notify()
            return element

    def size(self) -> int:
        with self.lock:
            return len(self.queue)