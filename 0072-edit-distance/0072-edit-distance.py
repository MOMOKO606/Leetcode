class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1) + 1, len(word2) + 1
        dp = [[0] * cols for _ in range(rows)]
        for j in range(1, cols): dp[0][j] = j
        for i in range(1, rows): dp[i][0] = i
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
        