class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        while j > 0 and nums[j - 1] >= nums[j]:
            j -= 1
        if j == 0: 
            nums.reverse()
            return
        i, j = j - 1, len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, len(nums) - 1
        while i < j and nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

        
        