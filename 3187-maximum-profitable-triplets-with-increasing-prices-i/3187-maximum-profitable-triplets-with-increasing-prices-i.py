class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        pre_max, post_max, ans = [-inf] * n, [-inf] * n, -1 
        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[i] < prices[j]:
                    post_max[i] = max(post_max[i], profits[j])
                    pre_max[j] = max(pre_max[j], profits[i])

        for i in range(n):
            ans = max(ans, pre_max[i] + profits[i] + post_max[i])
        return ans 
        