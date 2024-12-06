class FenwickTree:
    def __init__(self, size, value):
        self.size = size
        self.ft = [value] * size

    def __lowbit(self, index):
        return index & -index

    def update(self, index, value):
        while index < self.size:
            self.ft[index] = max(self.ft[index], value)
            index += self.__lowbit(index)
    
    def query(self, index):
        ans = -inf
        while index:
            ans = max(ans, self.ft[index])
            index -= self.__lowbit(index)
        return ans


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        max_price = max(prices)
        single, double, ans = FenwickTree(max_price + 1, 0), FenwickTree(max_price + 1, 0), -1
        for price, profit in zip(prices, profits):
            single.update(price, profit)
            max_single = single.query(price - 1)
            if max_single:
                double.update(price, profit + max_single)
            max_double = double.query(price - 1)
            if max_double:
                ans = max(ans, max_double + profit)
        return ans

            
        