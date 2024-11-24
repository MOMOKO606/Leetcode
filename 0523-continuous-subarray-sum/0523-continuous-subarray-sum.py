class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSums, preSum = {0: -1}, 0
        for j, num in enumerate(nums):
            preSum += num
            if preSum % k in preSums:
                if j - preSums[preSum % k] > 1: return True
            else: preSums[preSum % k] = j
        return False
        