class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        dp, ans = [[0, 0] for _ in range(len(nums))], 0
        dp[1][1] = nums[1] - nums[0]
        for i in range(2, len(nums)):
            prev_delta, delta = dp[i - 1][1], nums[i] - nums[i - 1]
            dp[i][1] = delta
            dp[i][0] = dp[i - 1][0] + 1 if prev_delta == delta else 0
            ans += dp[i][0]
        return ans
        