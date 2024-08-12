class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(i, amount):
            if not amount: return 0
            if amount < 0 or i == len(coins): return inf
            ans = inf
            for j in range(i, len(coins)):
                ans = min(ans, 1 + helper(j, amount - coins[j]))
            return ans

        ans = helper(0, amount)
        return ans if ans != inf else -1
        