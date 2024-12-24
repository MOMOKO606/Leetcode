class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        prefix, postfix, ans = [-inf] * len(prices), [-inf] * len(prices), -1
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    postfix[i] = max(postfix[i], profits[j])
                    prefix[j] = max(prefix[j], profits[i])
        
        for i in range(len(profits)):
            ans = max(ans, profits[i] + prefix[i] + postfix[i])
        return ans