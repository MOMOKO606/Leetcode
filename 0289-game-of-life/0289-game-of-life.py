class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        clones = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                clones[i][j] = board[i][j]
        
        for i in range(rows):
            for j in range(cols):
                ones, zeros = 0, 0
                for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1], [i - 1, j - 1], [i - 1, j + 1], [i + 1, j - 1], [i + 1, j + 1]]:
                    if not (0 <= x < rows and 0 <= y < cols): continue
                    if clones[x][y]: ones += 1
                    else: zeros += 1
                if not board[i][j] and ones == 3: board[i][j] = 1
                elif not (ones == 2 or ones == 3): board[i][j] = 0

                
