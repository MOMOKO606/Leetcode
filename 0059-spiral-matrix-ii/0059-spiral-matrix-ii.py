class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix, i, j, di, dj, cur = [[0] * n for _ in range(n)], 0, 0, 0, 1, 1
        while cur <= n * n:
            matrix[i][j] = cur
            if not (0 <= i + di < n and 0 <= j + dj < n) or matrix[i + di][j + dj]:
                di, dj = dj, -di
            i, j, cur = i + di, j + dj, cur + 1
        return matrix

        