class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs_helper(i, j):
            if not (0 <= i < rows and 0 <= j < cols and image[i][j] == ori_color): return
            image[i][j] = "#"
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                dfs_helper(x, y)



        rows, cols, ori_color = len(image), len(image[0]), image[sr][sc]
        dfs_helper(sr, sc)
        for i in range(rows):
            for j in range(cols):
                if image[i][j] == "#":
                    image[i][j] = color
        return image

        