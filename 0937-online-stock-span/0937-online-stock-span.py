class StockSpanner:

    def __init__(self):
        self.stack = [(0, inf)]
        self.index = 0
        

    def next(self, price: int) -> int:
        self.index += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        ans = self.index - self.stack[-1][0]
        self.stack.append((self.index, price))
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)