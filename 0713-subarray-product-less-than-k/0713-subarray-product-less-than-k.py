class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, value, ans = 0, 1, 0
        for j in range(len(nums)):
            while i <= j and value * nums[j] >= k:
                value /= nums[i]
                i += 1
            value *= nums[j]
            ans += j - i + 1
        return ans
                

        