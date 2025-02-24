from threading import Condition, Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.lock = Lock()
        self.capacity = capacity
        self.queue = []
        self.space_available = Condition(self.lock)
        self.item_available = Condition(self.lock)
        

    def enqueue(self, element: int) -> None:
        with self.lock:
            while len(self.queue) == self.capacity:
                self.space_available.wait()
            self.queue.append(element)
            self.item_available.notify()
    

    def dequeue(self) -> int:
        with self.lock:
            while len(self.queue) == 0:
                self.item_available.wait()
            element = self.queue.pop(0)
            self.space_available.notify()
            return element
        

    def size(self) -> int:
        with self.lock:
            return len(self.queue)
        