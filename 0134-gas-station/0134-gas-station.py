class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta, cur, start = 0, 0, 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
            delta += gas[i] - cost[i]
        return start if delta >= 0 else -1
        