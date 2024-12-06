class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        left, right, ans = [-inf] * len(prices), [-inf] * len(prices), -1
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    right[i] = max(right[i], profits[j])
                    left[j] = max(left[j], profits[i])
        for i in range(len(prices)):
            ans = max(ans, profits[i] + left[i] + right[i])
        return ans 

        