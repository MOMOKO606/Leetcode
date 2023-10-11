class RecentCounter:

    def __init__(self):
        self.deque = collections.deque([])
        

    def ping(self, t: int) -> int:
        left = t - 3000
        self.deque.append(t)
        while self.deque[0] < left:
            self.deque.popleft()
        return len(self.deque)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)