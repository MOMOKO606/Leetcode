class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def helper(i, prev):
            if i == len(nums): return []
            ans, possible = helper(i + 1, prev), []
            if not nums[i] % prev:
                possible = [nums[i]] + helper(i + 1, nums[i])
            return ans if len(ans) > len(possible) else possible

        nums = sorted(nums)
        return helper(0, 1)
        