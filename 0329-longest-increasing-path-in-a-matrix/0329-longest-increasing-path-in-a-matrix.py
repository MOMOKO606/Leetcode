class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfsHelper(i, j):
            if not (0 <= i < rows and 0 <= j < cols) or matrix[i][j] == "#": return 0
            ans = 0
            ori = matrix[i][j]
            matrix[i][j] = "#"
            for x, y in [[i + 1, j], [i - 1, j],[i, j - 1], [i, j + 1]]:
                if not (0 <= x < rows and 0 <= y < cols and matrix[x][y] != "#" and matrix[x][y] < ori): continue
                ans = max(ans, dfsHelper(x, y))
            matrix[i][j] = ori
            return ans + 1

        
        rows, cols, ans = len(matrix), len(matrix[0]), 1
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfsHelper(i, j))
        return ans

