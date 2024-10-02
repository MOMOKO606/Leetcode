class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        if left < len(nums) and nums[left] == target: return [left, right - 1]
        else: return [-1, -1]
        