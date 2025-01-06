class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, zeros, ans = -1, 0, 0
        for j, num in enumerate(nums):
            if not num: zeros += 1
            while zeros > 1:
                i += 1
                if not nums[i]: zeros -= 1
            ans = max(ans, j - i)
        return ans - 1


        