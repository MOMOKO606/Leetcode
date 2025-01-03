class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def helper(i=0, cur_total=0):
            if i == len(stones): return abs(cur_total)
            return min(helper(i + 1, cur_total + stones[i]), helper(i + 1, cur_total - stones[i]))

        return helper()
        