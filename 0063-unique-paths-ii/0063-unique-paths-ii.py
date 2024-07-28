class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def helper(i, j):
            if not (0 <= i < rows and 0 <= j < cols) or obstacleGrid[i][j]: return 0
            if i == 0 and j == 0: return 1
            return helper(i - 1, j) + helper(i, j - 1)
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        return helper(rows - 1, cols - 1)
