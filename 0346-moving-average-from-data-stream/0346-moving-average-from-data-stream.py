class MovingAverage:

    def __init__(self, size: int):
        self.count = 0
        self.total = 0    
        self.size = size    
        self.deque = deque([])

    def next(self, val: int) -> float:
        if self.count < self.size:
            self.count += 1 
        else:
            self.total -= self.deque.popleft()
        self.total += val
        self.deque.append(val)
        return self.total / self.count

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)