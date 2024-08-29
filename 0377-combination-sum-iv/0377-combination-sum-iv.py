class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(1, len(dp)):
            for num in nums:
                if j >= num: dp[j] += dp[j - num]
        return dp[-1]  

        