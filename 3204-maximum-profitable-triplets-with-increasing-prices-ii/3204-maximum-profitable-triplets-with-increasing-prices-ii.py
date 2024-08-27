# Modified Fenwick Tree for maximum num in nums[:index + 1]
class Fenwick:
    def __init__(self, n, original_value):
        self.size = n
        self.tree = [original_value] * n

    def _lowbit(self, index):
        return index & -index

    def update(self, index, num):
        while index < self.size:
            self.tree[index] = max(self.tree[index], num)
            index += self._lowbit(index)

    def query(self, index):
        ans = -1
        while index > 0:
            ans = max(ans, self.tree[index])
            index -= self._lowbit(index)
        return ans
        

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n, ans = max(prices), -1
        single, pair = Fenwick(n + 1, -1), Fenwick(2 * n + 1, -1)
        for price, profit in zip(prices, profits):
            pair_max = pair.query(price - 1)
            if pair_max > 0:
                ans = max(ans, pair_max + profit)
            
            single_max = single.query(price - 1)
            if single_max > 0:
                pair.update(price, single_max + profit)
            single.update(price, profit)
        return ans

            




        