class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        backup = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                backup[i][j] = matrix[i][j]

        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        while top < bottom:
            for j in range(left, right + 1):
                matrix[j][right] = backup[top][j]
            for i in range(top, bottom + 1):
                matrix[bottom][top + bottom - i] = backup[i][right]
            for j in range(left, right + 1):
                matrix[j][left] = backup[bottom][j]
            for i in range(top, bottom + 1):
                matrix[top][top + bottom - i] = backup[i][left]
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1

        