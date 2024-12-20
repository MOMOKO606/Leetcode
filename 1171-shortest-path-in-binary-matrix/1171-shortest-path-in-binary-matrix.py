class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1
        rows, cols, queue, ans = len(grid), len(grid[0]), [[0, 0]], 1
        while queue:
            next_queue = []
            for i, j in queue:
                if (i, j) == (rows - 1, cols - 1): return ans
                for x, y in [[i - 1, j - 1], [i, j - 1], [i + 1, j - 1], [i - 1, j], [i + 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1]]:
                    if not (0 <= x < rows and 0 <= y < cols and not grid[x][y]): continue
                    grid[x][y] = 1
                    next_queue.append([x, y])
            queue, ans = next_queue, ans + 1
        return -1



        