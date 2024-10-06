class FenwickTree:
    def __init__(self, value, size):
        self.tree = [value] * size
        self.size = size

    def __lowbit(self, index):
        return index & -index

    def update(self, index, value):
        while index < self.size:
            self.tree[index] = max(self.tree[index], value)
            index += self.__lowbit(index)
            
    def query(self, index):
        ans = -inf
        while index:
            ans = max(ans, self.tree[index])
            index -= self.__lowbit(index)
        return ans


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        largest_price = max(prices)
        single, double, ans = FenwickTree(0, largest_price + 1), FenwickTree(0, largest_price * 2 + 1), -1
        for price, profit in zip(prices, profits):
            single.update(price, profit)
            single_max = single.query(price - 1)
            if single_max:
                double.update(price, single_max + profit)
            double_max = double.query(price - 1)
            if double_max:
                ans = max(ans, double_max + profit)
        return ans
        
        