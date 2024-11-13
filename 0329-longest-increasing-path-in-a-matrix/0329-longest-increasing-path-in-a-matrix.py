class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(i, j):
            ans = 1
            for x, y in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < rows and 0 <= y < cols and matrix[i][j] > matrix[x][y]:
                    ans = max(ans, 1 + helper(x, y))
            return ans

        rows, cols, ans = len(matrix), len(matrix[0]), 1
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, helper(i, j))
        return ans

        