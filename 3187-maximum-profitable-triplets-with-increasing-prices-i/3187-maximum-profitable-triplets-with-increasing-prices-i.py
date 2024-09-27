class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        preMax, postMax, ans = [-inf] * len(prices), [-inf] * len(prices), -inf
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    preMax[j] = max(preMax[j], profits[i])
                    postMax[i] = max(postMax[i], profits[j])
        for i in range(len(prices)): 
            ans = max(ans, profits[i] + preMax[i] + postMax[i])
        return ans if ans != -inf else -1




        