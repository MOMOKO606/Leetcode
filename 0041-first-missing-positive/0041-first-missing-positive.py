class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            j = nums[i] - 1
            while 0 <= j < len(nums) and i + 1 != nums[i] and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1
        for i, num in enumerate(nums):
            if i + 1 != num: return i + 1
        return len(nums) + 1
        