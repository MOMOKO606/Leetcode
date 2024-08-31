class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        pre_max, post_max, ans = [-inf] * len(prices), [-inf] * len(prices), -1
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    pre_max[j] = max(pre_max[j], profits[i])
                    post_max[i] = max(post_max[i], profits[j])
        for i in range(len(prices)):
            ans = max(ans, pre_max[i] + post_max[i] + profits[i])
        return ans 

        