class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, ans = -1, inf
        for j in range(len(nums)):
            target -= nums[j]
            while i < len(nums) and target <= 0:
                ans = min(ans, j - i)
                i += 1
                if i < len(nums): target += nums[i]
        return ans if ans != inf else 0
        