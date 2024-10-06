class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            visited = {}
            for k in range(i + 1, len(nums)):
                if -nums[k] % d in visited: ans += visited[-nums[k] % d]
                visited[(nums[i] + nums[k]) % d] = visited.get((nums[i] + nums[k]) % d, 0) + 1
        return ans


        