class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = -1
        for j, num in enumerate(nums):
            if num != val:
                i += 1
                nums[i] = num
        return i + 1
        