class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(i, amount):
            if not amount: return 0
            if amount < 0 or i == len(coins): return inf
            return min(1 + helper(i, amount - coins[i]), helper(i + 1, amount))

        ans = helper(0, amount)
        return ans if ans != inf else -1
        