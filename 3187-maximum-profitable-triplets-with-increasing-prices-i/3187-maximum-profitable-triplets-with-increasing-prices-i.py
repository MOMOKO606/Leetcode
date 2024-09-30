class FenwickTree:
    def __init__(self, size, value):
        self.tree = [value] * size
        self.size = size

    def __lowbit(self, index):
        return index & -index

    def update(self, index, value):
        while index < self.size:
            self.tree[index] = max(self.tree[index], value)
            index += self.__lowbit(index)

    def query(self, index):
        ans = 0
        while index:
            ans = max(ans, self.tree[index])
            index -= self.__lowbit(index)
        return ans


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        largest = max(prices)
        single, double, ans = FenwickTree(largest + 1, 0), FenwickTree(2 * largest + 1, 0), -1
        for price, profit in zip(prices, profits):
            single.update(price, profit)
            single_max = single.query(price - 1)
            if single_max: 
                double.update(price, single_max + profit)
            double_max = double.query(price - 1)
            if double_max: ans = max(ans, double_max + profit)
        return ans

        