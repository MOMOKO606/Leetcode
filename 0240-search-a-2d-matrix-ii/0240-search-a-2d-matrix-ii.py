class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, cols - 1
        while 0 <= i < rows and 0 <= j < cols:
            if matrix[i][j] == target: return True
            elif matrix[i][j] < target: i += 1
            else: j -= 1
        return False
        