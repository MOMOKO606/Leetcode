class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols, i, j, di, dj, ans, visited = len(matrix), len(matrix[0]), 0, 0, 0, 1, [], set([])
        n = rows * cols
        while n:
            ans.append(matrix[i][j])
            visited.add((i, j))
            if not (0 <= i + di < rows and 0 <= j + dj < cols) or (di + i, j + dj) in visited:
                di, dj = dj, -di
            i, j = i + di, j + dj
            n -= 1
        return ans

        