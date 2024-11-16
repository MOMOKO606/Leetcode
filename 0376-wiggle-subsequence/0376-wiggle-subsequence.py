class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        prev = nums[1] - nums[0]
        ans = 2 if prev != 0 else 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (prev >= 0 and diff < 0) or (prev <= 0 and diff > 0):
                ans, prev = ans + 1, diff
        return ans

        