class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, cur, i = 0, 1, -1
        for j in range(len(nums)):
            cur *= nums[j]
            while i < j and cur >= k:
                i += 1
                cur /= nums[i]
            ans += j - i
        return ans
              

        