class FenwickTree:
    def __init__(self, size, original_value):
        self.size = size
        self.tree = [original_value] * size

    def __lowbit(self, index):
        return index & -index

    def update(self, index, num):
        while index < self.size:
            self.tree[index] = max(self.tree[index], num)
            index += self.__lowbit(index)

    def query(self, index):
        ans = -inf
        while index:
            ans = max(ans, self.tree[index])
            index -= self.__lowbit(index)
        return ans

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = max(prices)
        ans, single, double = -1, FenwickTree(n + 1, 0), FenwickTree(2 * n + 1, 0)
        for price, profit in zip(prices, profits):
            single.update(price, profit)

            single_max = single.query(price - 1)
            if single_max: double.update(price, single_max + profit)

            double_max = double.query(price - 1)
            if double_max: ans = max(ans, double_max + profit)

        return ans
        
        