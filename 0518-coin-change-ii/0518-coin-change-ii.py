class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def helper(i=0, amount=amount):
            if not amount: return 1
            if amount < 0 or i == len(coins): return 0
            return helper(i, amount - coins[i]) + helper(i + 1, amount)
        return helper()
        