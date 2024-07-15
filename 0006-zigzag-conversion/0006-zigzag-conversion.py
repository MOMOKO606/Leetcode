class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        s, cur_dirc_i, cur_dirc_j, matrix, i, j, ans = list(s), 1, 0, [[None] * len(s) for _ in range(numRows)], 0, 0, ""
        while s:
            char = s.pop(0)
            matrix[i][j] = char
            if i + cur_dirc_i == numRows:
                cur_dirc_i, cur_dirc_j = -1, 1
            elif i + cur_dirc_i == -1:
                cur_dirc_i, cur_dirc_j = 1, 0
            i += cur_dirc_i
            j += cur_dirc_j
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]: ans += matrix[i][j]
        return ans

        