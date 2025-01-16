class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = [set([i for i in range(1, n + 1)]) for _ in range(n)]
        cols = [set([i for i in range(1, n + 1)]) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                if not (num in rows[i] and num in cols[j]): return False
                rows[i].remove(num)
                cols[j].remove(num)
        return True