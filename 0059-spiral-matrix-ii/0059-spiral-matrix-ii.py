class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        N, cur, i, j, di, dj = n * n, 1, 0, 0, 0, 1
        ans = [[0] * n for _ in range(n)]
        while N:
            ans[i][j] = cur
            if not (0 <= i + di < n and 0 <= j + dj < n and not ans[i + di][j + dj]):
                di, dj = dj, -di
            i, j, cur, N = i + di, j + dj, cur + 1, N - 1
        return ans
        