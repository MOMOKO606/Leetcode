class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def helper(i):
            if i > len(cost) - 1: return 0
            return cost[i] + min(helper(i + 1), helper(i + 2))

        return min(helper(0), helper(1))

        