class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSums, preSum, ans = {0: 1}, 0, 0
        for num in nums:
            preSum += num
            if preSum - k in preSums: ans += preSums[preSum - k]
            preSums[preSum] = preSums.get(preSum, 0) + 1
        return ans


        