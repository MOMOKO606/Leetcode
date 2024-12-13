class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: 
        target, queue,  rows, cols = image[sr][sc], [[sr, sc]], len(image), len(image[0])
        if target == color: return image
        image[sr][sc] = color
        while queue:
            next_queue = []
            for i, j in queue:
                for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if not (0 <= x < rows and 0 <= y < cols and image[x][y] == target): continue
                    next_queue.append([x, y])
                    image[x][y] = color
            queue = next_queue
        return image

        