class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfsHelper(i, j):
            if not (0 <= i < rows and 0 <= j < cols and grid[i][j] == "1"): return 0
            grid[i][j] = "0"
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                dfsHelper(x, y)
            return 1

        rows, cols, ans = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                ans += dfsHelper(i, j)
        return ans

        