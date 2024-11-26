class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0] * (k + 1)
        self.k = k
        self.last = 0
        self.front = k
        self.count = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.deque[self.front] = value
        self.front = self.front - 1 if self.front > 0 else self.k
        self.count += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.deque[self.last] = value
        self.last = self.last + 1 if self.last < self.k else 0
        self.count += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.front = self.front + 1 if self.front < self.k else 0
        self.count -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.last = self.last - 1 if self.last > 0  else self.k
        self.count -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        i = self.front + 1 if self.front < self.k else 0
        return self.deque[i]
        

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        i = self.last - 1 if self.last > 0 else self.k
        return self.deque[i]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()