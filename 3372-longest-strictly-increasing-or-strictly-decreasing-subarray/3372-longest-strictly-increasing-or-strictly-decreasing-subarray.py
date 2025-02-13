class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase_count, decrease_count, ans = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increase_count, decrease_count = increase_count + 1, 1
            elif nums[i] < nums[i - 1]:
                increase_count, decrease_count = 1, decrease_count + 1
            else:
                increase_count, decrease_count = 1, 1
            ans = max(ans, increase_count, decrease_count)
        return ans
