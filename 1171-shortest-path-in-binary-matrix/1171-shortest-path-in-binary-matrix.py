class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] or grid[rows - 1][cols - 1]: return -1
        ans, queue = 1, [[0, 0]]
        while queue:
            next_queue = []
            for i, j in queue:
                if (i, j) == (rows - 1, cols - 1): return ans
                for di, dj in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    if not (0 <= i + di < rows and 0 <= j + dj < cols and not grid[i + di][j + dj]): continue
                    grid[i + di][j + dj] = 1
                    next_queue.append([i + di, j + dj])
            queue, ans = next_queue, ans + 1
        return -1

