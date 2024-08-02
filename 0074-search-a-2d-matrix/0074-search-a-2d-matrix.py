class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        i, j = rows - 1, 0
        while 0 <= i < rows and 0 <= j < cols:
            key = matrix[i][j]
            if target == key: return True
            elif target > key: j += 1
            else: i -= 1
        return False

        