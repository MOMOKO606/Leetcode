class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 1]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        return i + 1