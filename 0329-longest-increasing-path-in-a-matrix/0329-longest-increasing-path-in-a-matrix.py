class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(i, j):
            if not (0 <= i < rows and 0 <= j < cols and matrix[i][j] != "$"): 
                return 0
            ori = matrix[i][j]
            count, longest, matrix[i][j] = 1, 0, "$"
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] != "$" and matrix[x][y] < ori:
                    longest = max(longest, helper(x, y))
            matrix[i][j] = ori
            return count + longest
        
        rows, cols, ans = len(matrix), len(matrix[0]), 1
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, helper(i, j))
        return ans

        

        