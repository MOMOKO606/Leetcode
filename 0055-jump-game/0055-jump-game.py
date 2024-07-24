class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            if i > reach: return False
            if reach >= len(nums) - 1: return True
            reach = max(reach, i + num)
