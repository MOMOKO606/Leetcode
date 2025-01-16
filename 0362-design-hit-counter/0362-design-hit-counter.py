class HitCounter:

    def __init__(self):
        self.board = OrderedDict()
        self.total_hits = 0
        

    def hit(self, timestamp: int) -> None:
        self.board[timestamp] = self.board.get(timestamp, 0) + 1
        self.total_hits += 1
        

    def getHits(self, timestamp: int) -> int:
        left = max(timestamp - 300, 0)
        while self.board and next(iter(self.board.keys())) <= left:
            self.total_hits -= self.board.popitem(last=False)[1]
        return self.total_hits
      


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)