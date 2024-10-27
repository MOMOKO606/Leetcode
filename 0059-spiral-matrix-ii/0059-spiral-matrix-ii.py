class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix, i, j, di, dj, remain, cur = [[0] * n for _ in range(n)], 0, 0, 0, 1, n * n, 1
        while remain:
            matrix[i][j] = cur
            if not (0 <= i + di < n and 0 <= j + dj < n and matrix[i + di][j + dj] == 0):
                di, dj = dj, -di
            remain, cur, i, j = remain - 1, cur + 1, i + di, j + dj
        return matrix
        

        