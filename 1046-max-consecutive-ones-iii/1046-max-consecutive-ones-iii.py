class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, ones, ans = -1, 0, 0
        for j, num in enumerate(nums):
            if num: ones += 1
            while ones + k < j - i:
                i += 1
                if nums[i]: ones -= 1
            ans = max(ans, j - i)
        return ans