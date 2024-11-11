class Solution:
    @cache
    def numSquares(self, n: int) -> int:
        if not n: return 0
        if n < 0: return inf
        ans = n
        for num in reversed(range(1, int(n ** 0.5) + 1)):
            ans = min(ans, 1 + self.numSquares(n - num * num))
        return ans

        