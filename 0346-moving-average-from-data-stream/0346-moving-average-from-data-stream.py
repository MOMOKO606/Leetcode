class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.total = 0
        self.nums = []
        

    def next(self, val: int) -> float:
        if self.count == self.size:
            self.total -= self.nums.pop(0)
            self.count -= 1
        self.nums.append(val)
        self.total += val
        self.count += 1
        return self.total / self.count
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)