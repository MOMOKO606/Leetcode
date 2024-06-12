class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        reach, steps, next_reach = nums[0], 1, -inf
        for i, num in enumerate(nums):
            if reach >= len(nums) - 1: return steps
            next_reach = max(next_reach, i + num)
            if i == reach: reach, next_reach, steps = next_reach, -inf, steps + 1
            

        