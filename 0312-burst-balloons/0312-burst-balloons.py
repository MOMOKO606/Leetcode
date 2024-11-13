class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def helper(i, j):
            if i > j: return 0
            ans = -inf
            for k in range(i, j + 1):
                ans = max(ans, nums[i - 1] * nums[k] * nums[j + 1] + helper(i, k - 1) + helper(k + 1, j))
            return ans

        nums = [1] + nums + [1]
        return helper(1, len(nums) - 2)

        