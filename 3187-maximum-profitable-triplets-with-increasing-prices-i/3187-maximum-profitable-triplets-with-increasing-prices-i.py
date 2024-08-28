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
        ans = 0
        while index:
            ans = max(ans, self.tree[index])
            index -= self.__lowbit(index)
        return ans

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        max_price, ans = max(prices), -1
        single = FenwickTree(max_price + 1, 0)
        double = FenwickTree(max_price * 2 + 1 + 1, 0)
        for price, profit in zip(prices, profits):
            # Update single
            single.update(price, profit)
            
            # Update double
            single_max = single.query(price - 1)
            if single_max:
                double.update(price, profit + single_max)
            
            # Update ans
            double_max = double.query(price - 1)
            if double_max: ans = max(ans, double_max + profit)

            
        return ans




        