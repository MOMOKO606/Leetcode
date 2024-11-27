class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, ans, curProduct = -1, 0, 1
        for j, num in enumerate(nums):
            curProduct *= num
            while i < j and curProduct >= k:
                i += 1
                curProduct //= nums[i]
            ans += j - i
        return ans
        