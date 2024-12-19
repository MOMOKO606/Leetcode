class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfsHelper(i, j, remain):
            if (i, j) == end: return not remain
            if not (0 <= i < rows and 0 <= j < cols and remain and not grid[i][j]): return 0
            ans, grid[i][j] = 0, -1
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                ans += dfsHelper(x, y, remain - 1)
            grid[i][j] = 0
            return ans
        
        
        rows, cols, remain = len(grid), len(grid[0]), 1
        for i in range(rows):
            for j in range(cols):
                if not grid[i][j]: remain += 1
                elif grid[i][j] == 1: start, grid[i][j] = (i, j), 0
                elif grid[i][j] == 2: end = (i, j)
        return dfsHelper(start[0], start[1], remain)
        
        

        