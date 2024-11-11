class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j, num in enumerate(nums):
            if num != 0:
                nums[i], nums[j], i = nums[j], nums[i], i + 1

        