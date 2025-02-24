import threading

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []  # 用于存储队列元素的列表
        self.cv = threading.Condition()  # 通用的条件变量

    def enqueue(self, element: int) -> None:
        with self.cv:  # 获取锁
            while len(self.queue) == self.capacity:  # 如果队列已满
                self.cv.wait()  # 等待队列未满的条件
            self.queue.append(element)  # 添加元素
            self.cv.notify_all()  # 唤醒所有等待的线程（包括生产者和消费者）

    def dequeue(self) -> int:
        with self.cv:  # 获取锁
            while len(self.queue) == 0:  # 如果队列为空
                self.cv.wait()  # 等待队列非空的条件
            element = self.queue.pop(0)  # 移除元素
            self.cv.notify_all()  # 唤醒所有等待的线程（包括生产者和消费者）
            return element

    def size(self) -> int:
        with self.cv:  # 获取锁
            return len(self.queue)