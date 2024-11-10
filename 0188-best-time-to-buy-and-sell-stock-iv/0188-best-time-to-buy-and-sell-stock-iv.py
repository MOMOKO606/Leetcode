class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buys, sells = [-prices[0]] * k, [0] * k
        for price in prices:
            for i in range(k):
                buys[i] = max(buys[i], sells[i - 1] - price) if i > 0 else max(buys[i], -price)
                sells[i] = max(sells[i], buys[i] + price)
        return sells[-1]
        