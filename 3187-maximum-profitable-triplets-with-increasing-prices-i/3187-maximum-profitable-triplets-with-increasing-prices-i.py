class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        pre, post, ans = [-inf] * n, [-inf] * n, -inf
        for i in range(n - 1):
            for j in range(i + 1, n):
                if prices[i] < prices[j]:
                    pre[j] = max(pre[j], profits[i])
                    post[i] = max(post[i], profits[j])
        
        for i in range(1, n - 1):
            ans = max(ans, pre[i] + profits[i] + post[i])
        return ans if ans != -inf else -1
        