class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows, cols = numRows, len(s)
        matrix = [[None for j in range(cols)] for i in range(rows)]
        
        i, j, di, dj = 0, 0, 1, 0
        for char in s:
            matrix[i][j] = char
            if i + di == rows:
                di, dj = -1, 1
            elif i + di == -1:
                di, dj = 1, 0
            i, j = i + di, j + dj
        
        ans = ""
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]: ans += matrix[i][j]
        return ans

        