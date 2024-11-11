class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(i, j):
            if not (0 <= i < rows and 0 <= j < cols): return False
            if matrix[i][j] == target: return True
            if matrix[i][j] > target:
                return helper(i, j - 1)
            else:
                return helper(i + 1, j)
        
        
        rows, cols = len(matrix), len(matrix[0])
        return helper(0, cols - 1)

        