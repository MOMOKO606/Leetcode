class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for j in range(len(nums)):
            if nums[j] == 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        k = i
        for j in range(k + 1, len(nums)):
            if nums[j] == 1:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        