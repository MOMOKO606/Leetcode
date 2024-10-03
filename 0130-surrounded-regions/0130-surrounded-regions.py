class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(i, j):
            deque = collections.deque([[i, j]])
            while deque:
                i, j = deque.popleft()
                for x, y in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
                    if not (0 <= x < rows and 0 <= y < cols and board[x][y] == "O"): continue
                    board[x][y] = "$"
                    deque.append([x, y])


        rows, cols = len(board), len(board[0])
        for i in [0, rows - 1]:
            for j in range(cols):
                if board[i][j] == "X": continue
                board[i][j] = "$"
                helper(i, j)

        for j in [0, cols - 1]:
            for i in range(rows):
                if board[i][j] == "X": continue
                board[i][j] = "$"
                helper(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "$":
                    board[i][j] = "O"

        