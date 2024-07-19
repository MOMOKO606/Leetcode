class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set([i for i in range(10)]) for _ in range(9)]
        cols = [set([i for i in range(10)]) for _ in range(9)]
        blocks = [set([i for i in range(10)]) for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue
                num, k = int(board[i][j]), 3 * (i // 3) + j // 3
                if not num in rows[i] & cols[j] & blocks[k]: return False
                rows[i].remove(num)
                cols[j].remove(num)
                blocks[k].remove(num)
        return True
                


        