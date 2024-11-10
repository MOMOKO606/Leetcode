class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols, ans = len(matrix), len(matrix[0]), 0
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
        for i in range(rows):
            for j in range(cols):
                if not matrix[i][j]: continue
                if i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
                ans = max(ans, matrix[i][j])
        return ans * ans

        