class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, cur_product, ans = 0, 1, 0
        for j, num in enumerate(nums):
            cur_product *= num
            while i <= j and cur_product >= k:
                cur_product /= nums[i]
                i += 1
            ans += j - i + 1
        return ans
            
        