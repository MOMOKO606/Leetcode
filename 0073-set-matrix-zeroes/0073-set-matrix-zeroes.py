class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols, zero_in_row, zero_in_col = len(matrix), len(matrix[0]), False, False
        for i in range(rows): 
            if not matrix[i][0]: 
                zero_in_col = True
                break
        for j in range(cols): 
            if not matrix[0][j]: 
                zero_in_row = True
                break
        for i in range(rows):
            for j in range(cols):
                if not matrix[i][j]: matrix[0][j], matrix[i][0] = 0, 0
        for i in range(1, rows):
            if not matrix[i][0]:
                for j in range(1, cols):
                    matrix[i][j] = 0

        for j in range(1, cols):
            if not matrix[0][j]:
                for i in range(1, rows):
                    matrix[i][j] = 0

        if zero_in_row: 
            for j in range(cols):
                matrix[0][j] = 0
        if zero_in_col:
            for i in range(rows):
                matrix[i][0] = 0

        

        