class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i, j):
            queue = [[i, j]]
            while queue:
                next_queue = []
                for i, j in queue:
                    for x, y in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
                        if not (0 <= x < rows and 0 <= y < cols and grid[x][y] == "1"): continue
                        
                        next_queue.append([x, y])
                        grid[x][y] = "0"
                queue = next_queue
                

        rows, cols, ans = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0": continue
                ans += 1
                helper(i, j)
        return ans

        