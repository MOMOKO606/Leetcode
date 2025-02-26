class FenwickTree:
    def __init__(self, size, value):
        self.size = size
        self.nums = [value] * size

    def lowbit(self, index):
        return index & -index

    def update(self, index, value):
        while index < self.size:
            self.nums[index] = max(self.nums[index], value)
            index += self.lowbit(index)

    def query(self, index):
        ans = 0
        while index:
            ans = max(ans, self.nums[index])
            index -= self.lowbit(index)
        return ans


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        max_price = max(prices)
        single, double, ans = FenwickTree(max_price + 1, 0), FenwickTree(max_price + 1, 0), 0
        for price, profit in zip(prices, profits):
            single.update(price, profit)
            cur_single = single.query(price - 1)
            if cur_single:
                double.update(price, cur_single + profit)

            cur_double = double.query(price - 1)
            if cur_double:
                ans = max(ans, cur_double + profit)

        return ans if ans != 0 else -1

        