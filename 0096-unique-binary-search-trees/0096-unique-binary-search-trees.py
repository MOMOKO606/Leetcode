class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n < 2: return 1
        ans = 0
        for i in range(n):
            ans += self.numTrees(i) * self.numTrees(n - i - 1)
        return ans

        