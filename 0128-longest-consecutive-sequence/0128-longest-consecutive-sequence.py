class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, ans, longest = sorted(set(nums)), 0, 0
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] + 1 == num:
                longest += 1
            else: longest = 1
            ans = max(ans, longest)
        return ans

        