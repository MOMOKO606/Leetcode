class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols, queue, steps = len(maze), len(maze[0]), [], 0
        for i in [0, rows - 1]:
            for j in range(cols):
                if maze[i][j] == "." and [i, j] != entrance: queue.append([i, j])

        for j in [0, cols - 1]:
            for i in range(rows):
                if maze[i][j] == "." and [i, j] != entrance: queue.append([i, j])

        while queue:
            next_queue = []
            for i, j in queue:
                if [i, j] == entrance: return steps
                for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if not (0 <= x < rows and 0 <= y < cols and maze[x][y] == "."): continue
                    next_queue.append([x, y])
                    maze[x][y] = "+"
            steps, queue = steps + 1, next_queue
        return -1

        