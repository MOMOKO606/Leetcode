class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = -1
        for j, num in enumerate(nums):
            if not num & 1:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return nums
        