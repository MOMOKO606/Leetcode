class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy, sell = [-prices[0]] * k, [0] * k
        for price in prices:
            for i in range(k):
                buy[i] = max(buy[i], sell[i - 1] - price) if i > 0 else max(buy[i], -price)
                sell[i] = max(sell[i], buy[i] + price)
        return sell[-1]
        