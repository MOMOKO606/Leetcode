class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans, total, i = -math.inf, 0, 0
        for j, num in enumerate(nums):
            if j >= k: total, i = total - nums[i], i + 1
            total += num
            if j - i + 1 == k: ans = max(ans, total / k)
        return ans
        