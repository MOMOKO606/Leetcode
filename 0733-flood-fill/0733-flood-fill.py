class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols, ori_color, queue, visited, image[sr][sc] = len(image), len(image[0]), image[sr][sc], [(sr, sc)], set((sr, sc)), color
        while queue:
            next_queue = []
            for i, j in queue:
                for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= x < rows and 0 <= y < cols and image[x][y] == ori_color and (x, y) not in visited:
                        image[x][y] = color
                        visited.add((x, y))
                        next_queue.append([x, y])
            queue = next_queue
        return image

        