import queue
import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.queue = queue.Queue(maxsize=capacity)  # 使用 queue.Queue 实现有限阻塞队列

    def enqueue(self, element: int) -> None:
        self.queue.put(element)  # 阻塞直到队列有空闲空间

    def dequeue(self) -> int:
        return self.queue.get()  # 阻塞直到队列中有元素

    def size(self) -> int:
        return self.queue.qsize()  # 返回队列当前大小