class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for j, num in enumerate(nums):
            if target - num in visited: return visited[target - num], j
            else: visited[num] = j
             
