class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1
        dp = [[0] * cols for _ in range(rows)]
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = 1 + dp[i - 1][j - 1] if text1[i - 1] == text2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
                
        

        