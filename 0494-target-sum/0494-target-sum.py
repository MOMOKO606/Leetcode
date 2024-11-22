class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def helper(i=0, target=target):
            if i == len(nums): return not target
            return helper(i + 1, target - nums[i]) + helper(i + 1, target + nums[i])
        return helper()
            
        