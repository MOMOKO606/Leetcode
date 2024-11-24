class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def check_surround(i, j):
            count = 0
            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1], [i - 1, j - 1], [i - 1, j + 1], [i + 1, j - 1], [i + 1, j + 1]]:
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == "M":
                    count += 1
            return str(count) if count else "B"

        def helper(i, j):
            if not (0 <= i < rows and 0 <= j < cols and board[i][j] == "E"): return
            board[i][j] = check_surround(i, j)
            if board[i][j] == "B":
                for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1], [i - 1, j - 1], [i - 1, j + 1], [i + 1, j - 1], [i + 1, j + 1]]:
                    helper(x, y)
        
        rows, cols = len(board), len(board[0])
        if board[click[0]][click[1]] == "M": 
            board[click[0]][click[1]] = "X"
        elif board[click[0]][click[1]] == "E":
            helper(click[0], click[1])
        return board 
        