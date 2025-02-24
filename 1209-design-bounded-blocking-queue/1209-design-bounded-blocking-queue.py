from threading import Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = []
        self.capacity = capacity
        self.cv = Condition()
        

    def enqueue(self, element: int) -> None:
        with self.cv:
            while len(self.queue) == self.capacity:
                self.cv.wait()
            self.queue.append(element)
            self.cv.notify_all()
        

    def dequeue(self) -> int:
        with self.cv:
            while len(self.queue) == 0:
                self.cv.wait()
            element = self.queue.pop(0)
            self.cv.notify_all()
            return element
        

    def size(self) -> int:
        with self.cv:
            return len(self.queue)
        