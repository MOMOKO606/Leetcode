class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def helper(i=0, total=0):
            if i == len(stones): return abs(total)
            return min(helper(i + 1, total + stones[i]), helper(i + 1, total - stones[i]))

        return helper()
        