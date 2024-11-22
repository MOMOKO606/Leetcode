class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols, queue, visited = len(maze), len(maze[0]), [start], set([])
        while queue:
            nextQueue = []
            for x, y in queue:
                if [x, y] == destination: return True
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    i, j = x, y
                    while 0 <= i + di < rows and 0 <= j + dj < cols and not maze[i + di][j + dj]:
                        i, j = i + di, j + dj
                    if (i, j) not in visited:
                        nextQueue.append([i, j])
                        visited.add((i, j))
            queue = nextQueue
        return False
        