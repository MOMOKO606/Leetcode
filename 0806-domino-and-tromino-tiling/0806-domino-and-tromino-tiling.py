class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:  return n
        dp, MOD = [[0] * n for _ in range(3)], 10 ** 9 + 7
        dp[0][0] =  dp[1][1] = dp[2][1] = 1
        dp[0][1] = 2
        for i in range(2, n):
            dp[0][i] = (dp[0][i - 1] + dp[0][i - 2] + dp[1][i - 1] + dp[2][i - 1]) % MOD
            dp[1][i] = (dp[0][i - 2] + dp[2][i - 1]) % MOD
            dp[2][i] = (dp[0][i - 2] + dp[1][i - 1]) % MOD
        return dp[0][-1]        

        