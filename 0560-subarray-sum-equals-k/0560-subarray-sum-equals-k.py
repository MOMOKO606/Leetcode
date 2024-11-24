class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSums, preSum , ans = {0: 1}, 0, 0
        for num in nums:
            preSum += num
            ans += preSums.get(preSum - k, 0)
            preSums[preSum] = preSums.get(preSum, 0) + 1
        return ans

        