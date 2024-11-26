class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            if not (0 <= i < rows and 0 <= j < cols and grid[i][j]): return 0
            grid[i][j] = 0
            count = 1
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                count += helper(x, y)
            return count


        ans, rows, cols = 0, len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, helper(i, j))
        return ans
        
        