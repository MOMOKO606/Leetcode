class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top, bottom, left, right = 0, n - 1, 0, n - 1
        backup = [matrix[i][:] for i in range(n) ]
        while left < right:
            for j in range(left, right + 1):
                matrix[j][right] = backup[top][j]

            for i in range(top, bottom + 1):
                matrix[bottom][bottom + top - i] = backup[i][right]

            for j in range(left, right + 1):
                matrix[j][left] = backup[bottom][j]

            for i in range(top, bottom + 1):
                matrix[top][bottom + top - i] = backup[i][left]

            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
   
