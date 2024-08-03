class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfsHelper(i, j, k):
            if k == len(word): return True
            if not (0 <= i < rows and 0 <= j < cols) or board[i][j] != word[k]: return False
            ori = board[i][j]
            board[i][j] = "$"
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if dfsHelper(i + di, j + dj, k + 1): return True
            board[i][j] = ori
            return False 

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if dfsHelper(i, j, 0): return True
        return False

        