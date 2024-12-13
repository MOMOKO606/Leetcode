class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        dp = [0] * (max_num + 1)
        for num, freq in Counter(nums).items():
            dp[num] += num * freq
        if max_num < 2: return dp[max_num]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
        return dp[-1]
        

        