class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(i, j):
            if not (0 <= i < rows and 0 <= j < cols): return 0
            ans = 0
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if not (0 <= x < rows and 0 <= y < cols) or matrix[x][y] >= matrix[i][j]: continue
                ans = max(ans, helper(x, y))
            return ans + 1

        
        rows, cols, ans = len(matrix), len(matrix[0]), 1
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, helper(i, j))
        return ans
        