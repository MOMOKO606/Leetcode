class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev, increase_count, decrease_count, ans = nums[0], 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i] > prev:
                increase_count, decrease_count = increase_count + 1, 1
            elif nums[i] < prev:
                increase_count, decrease_count = 1, decrease_count + 1
            else:
                increase_count, decrease_count = 1, 1
            prev = nums[i]
            ans = max(ans, increase_count, decrease_count)
        return ans
