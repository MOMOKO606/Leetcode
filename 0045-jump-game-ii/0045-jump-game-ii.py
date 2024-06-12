class Solution:
    def jump(self, nums: List[int]) -> int:
        reach, nextReach, steps = 0, -math.inf, 0
        for i, num in enumerate(nums):
            if reach >= len(nums) - 1: return steps
            nextReach = max(nextReach, i + num)
            if i == reach: reach, steps = nextReach, steps + 1
            


        