class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            j = num - 1
            while 0 <= j < len(nums) and nums[i] != i + 1 and nums[j] != j + 1:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1
        for i, num in enumerate(nums):
            if num != i + 1: return i + 1
        return len(nums) + 1
        