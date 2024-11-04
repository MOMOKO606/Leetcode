class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows, cols = len(s) + 1, len(t) + 1
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows): dp[i][0] = 1
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] if s[i - 1] == t[j - 1] else dp[i - 1][j]
        return dp[-1][-1]
        