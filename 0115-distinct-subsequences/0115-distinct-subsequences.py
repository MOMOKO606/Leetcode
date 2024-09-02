class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows, cols = len(t) + 1, len(s) + 1
        dp = [[0] * cols for _ in range(rows)]
        for j in range(cols): dp[0][j] = 1
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = dp[i][j - 1]
                if t[i - 1] == s[j - 1]: dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]
        