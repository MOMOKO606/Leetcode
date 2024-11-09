class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            dp = nums[:]
            dp[1] = max(dp[0], dp[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        if len(nums) == 0: return []
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        return max(helper(nums[1:]), helper(nums[:-1]))
        