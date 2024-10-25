class Solution:
    def jump(self, nums: List[int]) -> int:
        reach, nextReach, count = 0, 0, 0
        for j, num in enumerate(nums):
            if reach >= len(nums) - 1: return count
            if j <= reach:
                nextReach = max(nextReach, j + num)
                if j == reach:
                    reach, count = nextReach, count + 1
        

        