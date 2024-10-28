class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        firstRow, firstCol = False, False
        for j in range(cols):
            if not matrix[0][j]: 
                firstRow = True
                break
        
        for i in range(rows):
            if not matrix[i][0]:
                firstCol = True
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if not matrix[i][j]:
                    matrix[0][j], matrix[i][0] = 0, 0


        for i in range(1, rows):
            for j in range(1, cols):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0

        if firstRow:
            for j in range(cols): matrix[0][j] = 0
        
        if firstCol:
            for i in range(rows): matrix[i][0] = 0