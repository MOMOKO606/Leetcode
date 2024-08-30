class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, value, ans = 0, 1, 0
        for j in range(len(nums)):
            value *= nums[j]
            while i <= j and value >= k:
                value //= nums[i]
                i += 1
            ans += j - i + 1
        return ans
                

        