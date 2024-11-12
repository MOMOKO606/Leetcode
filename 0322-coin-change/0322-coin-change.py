class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(amount=amount):
            if not amount: return 0
            if amount < 0: return inf
            ans = inf
            for coin in coins:
                ans = min(ans, 1 + helper(amount - coin))
            return ans

        ans = helper()
        return ans if ans != inf else -1
        