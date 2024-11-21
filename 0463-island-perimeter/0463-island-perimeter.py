class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols, ans = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if not grid[i][j]: continue
                ans += 4
                if i > 0 and grid[i - 1][j]: ans -= 1
                if i + 1 < rows and grid[i + 1][j]: ans -= 1
                if j > 0 and grid[i][j - 1]: ans -= 1
                if j + 1 < cols and grid[i][j + 1]: ans -= 1
        return ans

        