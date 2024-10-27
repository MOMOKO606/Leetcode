class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: return 1
        if m < 1 or n < 1: return 0
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        
        