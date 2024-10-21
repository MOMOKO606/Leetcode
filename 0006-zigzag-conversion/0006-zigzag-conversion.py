class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        matrix = [[""] * len(s) for _ in range(numRows)]
        i, j, di, dj = 0, 0, 1, 0
        for char in s:
            matrix[i][j] = char
            if i + di == numRows:
                di, dj = -1, 1
            elif i + di == -1:
                di, dj = 1, 0
            i, j = i + di, j + dj
        return "".join(["".join(matrix[i]) for i in range(numRows)])
        