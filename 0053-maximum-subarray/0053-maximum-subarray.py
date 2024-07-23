class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, cur_sum = -inf, 0
        for num in nums:
            if cur_sum < 0:
                cur_sum = num
            else:
                cur_sum += num
            ans = max(ans, cur_sum)
        return ans
        