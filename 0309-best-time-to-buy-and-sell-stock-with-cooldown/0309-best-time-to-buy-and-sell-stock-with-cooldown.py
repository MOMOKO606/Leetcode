class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = -prices[0], [0, 0]
        for price in prices:
            buy = max(buy, sell[0] - price)
            sell[0] = sell[1]
            sell[1] = max(sell[1], buy + price)
        return sell[-1]
        