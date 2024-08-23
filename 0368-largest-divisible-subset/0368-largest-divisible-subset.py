class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def helper(i, prev):
            if i == len(nums): return []
            ans, potential = helper(i + 1, prev), []
            if not nums[i] % prev:
                potential = [nums[i]] + helper(i + 1, nums[i])
            return ans if len(ans) > len(potential) else potential
        nums.sort()
        return helper(0, 1)
        