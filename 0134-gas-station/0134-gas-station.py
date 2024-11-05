class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nums = [g - c for g, c in zip(gas, cost)]
        if sum(nums) < 0: return -1
        nums += nums[:-1]
        total, largestTotal, ans, curLeftIndex = -inf, -inf, 0, 0
        for i, num in enumerate(nums):
            if total + num < num:
               total, curLeftIndex = num, i
            else: total += num
            if total > largestTotal:
                largestTotal, ans = total, curLeftIndex
        return ans


        