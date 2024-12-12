class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, num in enumerate(nums):
            right -= num
            if left == right: return i
            left += num
        return -1

        

        