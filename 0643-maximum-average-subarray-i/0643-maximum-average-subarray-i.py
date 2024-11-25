class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans, i, total = -inf, -1, 0
        for j, num in enumerate(nums):
            total += num
            if j - i > k:
                i += 1
                total -= nums[i]
            if j - i == k: ans = max(ans, total / k)
        return ans



        