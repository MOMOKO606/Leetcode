class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        ans, pre_max, post_max = -1, [-inf] * len(prices), [-inf] * len(prices)
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    pre_max[j] = max(pre_max[j], profits[i])
                    post_max[i] = max(post_max[i], profits[j])
        
        for profit_i, profit_j, profit_k in zip(pre_max, profits, post_max):
            ans = max(ans, profit_i + profit_j + profit_k)
        return ans



        