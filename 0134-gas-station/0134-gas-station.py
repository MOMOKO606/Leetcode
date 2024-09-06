class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nums = [g - c for g, c in zip(gas, cost)]
        total = sum(nums)
        if total < 0: return -1
        i, cur = 0, 0
        for j in range(len(nums)):
            cur += nums[j]
            while cur < 0:
                cur -= nums[i]
                i += 1
        return i if cur >= total - cur else -1


  


        