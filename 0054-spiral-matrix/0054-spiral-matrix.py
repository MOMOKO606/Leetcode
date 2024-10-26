class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols, ans, i, j, di, dj = len(matrix), len(matrix[0]), [], 0, 0, 0, 1
        remain = rows * cols
        while remain:
            ans.append(matrix[i][j])
            matrix[i][j] = "#"
            if not (0 <= i + di < rows and 0 <= j + dj < cols and matrix[i + di][j + dj] != "#"):
                di, dj = dj, -di
            i, j, remain = i + di, j + dj, remain - 1
        return ans

        