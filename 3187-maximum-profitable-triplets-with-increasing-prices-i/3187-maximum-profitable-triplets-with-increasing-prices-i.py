class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        ans, preMax, postMax = -1, [-inf] * len(prices), [-inf] * len(prices)
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    preMax[j] = max(preMax[j], profits[i])
                    postMax[i] = max(postMax[i], profits[j])

        for i in range(len(prices)):
            ans = max(ans, preMax[i] + postMax[i] + profits[i])
        return ans if ans != -inf else -1
        