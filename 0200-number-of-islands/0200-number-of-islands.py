class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i, j):
            if grid[i][j] == "0": return
            grid[i][j] = "0"
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if not (0 <= x < rows and 0 <= y < cols and grid[x][y] == "1"): continue
                helper(x, y)
                

        rows, cols, ans = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0": continue
                ans += 1
                helper(i, j)
        return ans

        