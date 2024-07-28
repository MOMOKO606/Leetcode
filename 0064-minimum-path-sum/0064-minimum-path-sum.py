class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def helper(i, j):
            if not i and not j: return grid[i][j]
            if not (0 <= i < rows and 0 <= j < cols): return inf
            return grid[i][j] + min(helper(i - 1, j), helper(i, j - 1))

        rows, cols = len(grid), len(grid[0])
        return helper(rows - 1, cols - 1)
        