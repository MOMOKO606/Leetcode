class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols, ans, i, j, di, dj, visited = len(matrix), len(matrix[0]), [], 0, 0, 0, 1, set([])
        n = rows * cols
        while n:
            ans.append(matrix[i][j])
            visited.add((i, j))
            if not (0 <= i + di < rows and 0 <= j + dj < cols and (i + di, j + dj) not in visited):
                di, dj = dj, -di
            i, j = i + di, j + dj
            n -= 1
        return ans
        