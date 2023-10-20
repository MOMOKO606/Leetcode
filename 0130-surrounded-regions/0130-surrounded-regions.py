class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfsHelper(i, j, symbol):
            if not (0 <= i < rows and 0 <= j < cols and board[i][j] == "O"): return 
            board[i][j] = symbol
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                dfsHelper(x, y, symbol)


        rows, cols = len(board), len(board[0])
        for j in [0, cols - 1]:
            for i in range(rows):
                dfsHelper(i, j, "$") 
        for i in [0, rows - 1]:
            for j in range(cols):
                dfsHelper(i, j, "$")
        for i in range(1, rows):
            for j in range(1, cols):
                dfsHelper(i, j, "X")
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "$": board[i][j] = "O"
        