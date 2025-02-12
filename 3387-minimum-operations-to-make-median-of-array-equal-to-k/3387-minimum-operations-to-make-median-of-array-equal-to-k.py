class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        mid, nums = len(nums) // 2, sorted(nums)
        ans, i, j = abs(nums[mid] - k), mid - 1, mid + 1
        while i >= 0 and nums[i] > k:
            i, ans = i - 1, ans + abs(nums[i] - k)
        while j < len(nums) and nums[j] < k:
            j, ans = j + 1, ans + abs(nums[j] - k)
        return ans
