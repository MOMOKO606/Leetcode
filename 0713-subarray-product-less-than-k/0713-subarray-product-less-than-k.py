class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, cur, ans = 0, 1, 0
        for j, num in enumerate(nums):
            cur *= num
            while i <= j and cur >= k:
                cur //= nums[i]
                i += 1
            ans += j - i + 1
        return ans