class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i, total, ans = -1, 0, 0
        for j, num in enumerate(nums):
            total += num
            while total * (j - i) >= k:
                i += 1
                total -= nums[i]
            ans += j - i
        return ans
        
        