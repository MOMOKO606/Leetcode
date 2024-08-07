class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] - 1 < len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i, num in enumerate(nums):
            if num != i + 1: return i + 1
        return len(nums) + 1
        
        