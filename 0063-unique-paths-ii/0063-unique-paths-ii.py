class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]: return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[-1][-1] = 1
        for j in range(cols - 2, -1, -1):
            dp[rows - 1][j] = dp[rows - 1][j + 1] if not obstacleGrid[rows - 1][j] else 0
        for i in range(rows - 2, -1, -1):
            dp[i][cols - 1] = dp[i + 1][cols - 1] if not obstacleGrid[i][cols - 1] else 0
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                dp[i][j] = 0 if obstacleGrid[i][j] else dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

        