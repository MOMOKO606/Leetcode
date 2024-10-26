class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, ans = 0, -inf
        for num in nums:
            if cur_sum + num < num: cur_sum = num
            else: cur_sum += num
            ans = max(ans, cur_sum)
        return ans
        