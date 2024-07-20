class Solution:
    def jump(self, nums: List[int]) -> int:
        reach, steps, next_reach = 0, 0, -inf
        for i, num in enumerate(nums):
            next_reach = max(next_reach, i + num)
            if reach >= len(nums) - 1:
                return steps
            if i == reach:
                reach, steps = next_reach, steps + 1
            
        
        