class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3: return n
        dp, MOD = [[0] * 3 for _ in range(n)], 10 ** 9 + 7
        dp[0][0] = dp[1][1] = dp[1][2] = 1
        dp[1][0] = 2
        for i in range(2, n):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][0] + dp[i - 2][0]) % MOD
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 2][0] + dp[i - 1][1]) % MOD
        return dp[-1][0]

        