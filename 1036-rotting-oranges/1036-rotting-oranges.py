class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:      
        rows, cols, steps, queue, remain = len(grid), len(grid[0]), 0, [], 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: queue.append([i, j])
                elif grid[i][j] == 1: remain += 1
        
        while queue and remain:
            next_queue = []
            for i, j in queue:
                for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        next_queue.append([x, y])
                        remain -= 1
                        grid[x][y] = 2
            queue, steps = next_queue, steps + 1
        return steps if not remain else -1

        