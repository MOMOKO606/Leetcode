class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def move(i, j, di, dj, top, bottom, left, right, k):
            ori, k = grid[i][j], k % ((right - left + 1) * 2 + (bottom - top - 1) * 2)
            while k:
                if not (top <= i + di <= bottom and left <= j + dj <= right ):
                    di, dj = -dj, di
                k, i, j = k - 1, i + di, j + dj
            ans[i][j] = ori

        
        rows, cols = len(grid), len(grid[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        ans = [[0] * cols for _ in range(rows)]
        while top < bottom and left < right:
            for j in range(left, right + 1): move(top, j, 0, -1, top, bottom, left, right, k)
            for j in range(left, right + 1): move(bottom, j, 0, 1, top, bottom, left, right, k)
            for i in range(top + 1, bottom): move(i, left, 1, 0, top, bottom, left, right, k)
            for i in range(top + 1, bottom): move(i, right, -1, 0, top, bottom, left, right, k)
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return ans

            

