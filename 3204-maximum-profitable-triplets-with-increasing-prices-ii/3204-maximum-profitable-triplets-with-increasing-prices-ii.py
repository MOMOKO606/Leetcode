class FenwickTree:
    def __init__(self, value, size):
        self.size = size
        self.nums = [value] * size

    def lowbit(self, index):
        return index & -index

    def update(self, i, value):
        while i < self.size:
            self.nums[i] = max(self.nums[i], value)
            i += self.lowbit(i)

    def query(self, i):
        ans = -inf
        while i:
            ans = max(ans, self.nums[i])
            i -= self.lowbit(i)
        return ans


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        max_price = max(prices)
        single, double, ans = FenwickTree(0, max_price + 1), FenwickTree(0, max_price + 1), -1
        for price, profit in zip(prices, profits):
            single.update(price, profit)
            single_max = single.query(price - 1)
            if single_max:
                double.update(price, profit + single_max)
            double_max = double.query(price - 1)
            if double_max:
                ans = max(ans, double_max + profit)
        return ans

        