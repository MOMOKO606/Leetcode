class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfsHelper(i, j):
            ans = 0
            for x, y in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                    ans = max(ans, dfsHelper(x, y))
            return ans + 1
            

        rows, cols, ans = len(matrix), len(matrix[0]), 1
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfsHelper(i, j))
        return ans
        