class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, cur, ans = -1, 0, -inf
        for j in range(len(nums)):
            cur += nums[j]
            if j > k - 1:
                i += 1
                cur -= nums[i]
            if j - i == k:
                ans = max(ans, cur / (j - i))
        return ans
        