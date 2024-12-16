class RecentCounter:

    def __init__(self):
        self.times = collections.deque()
        self.count = 0
        

    def ping(self, t: int) -> int:
        target = t - 3000
        while self.times and self.times[0] < target:
            self.times.popleft()
            self.count -= 1
        self.times.append(t)
        self.count += 1
        return self.count

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)