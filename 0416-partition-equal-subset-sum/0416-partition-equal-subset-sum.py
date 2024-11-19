class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def helper(i, target):
            if not target: return True
            if i == len(nums) or target < 0: return False
            return helper(i + 1, target - nums[i]) or helper(i + 1, target)

        total = sum(nums)
        if total & 1: return False
        target = total // 2
        return helper(0, target)
        