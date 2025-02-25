class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            visited = {}
            for j in range(i + 1, len(nums)):
                if -nums[j] % d in visited:
                    ans += visited[-nums[j] % d]
                visited[(nums[i] + nums[j]) % d] = visited.get((nums[i] + nums[j]) % d, 0) + 1
        return ans


        