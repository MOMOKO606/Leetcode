class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = -1
        for k, num in enumerate(nums):
            if num == 0:
                i, j = i + 1, j + 1
                nums[i], nums[k] = nums[k], nums[i]
                if j != i: nums[j], nums[k] = nums[k], nums[j]
            elif num == 1:
                j += 1
                nums[j], nums[k] = nums[k], nums[j]
        