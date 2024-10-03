class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set([i for i in range(1, 10)]) for _ in range(9)]
        cols = [set([i for i in range(1, 10)]) for _ in range(9)]
        blocks = [set([i for i in range(1, 10)]) for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".": continue
                num, k = int(board[i][j]), (i // 3) * 3 + j // 3
                if num in rows[i] and num in cols[j] and num in blocks[k]:
                    rows[i].remove(num)
                    cols[j].remove(num)
                    blocks[k].remove(num)
                else: return False
        return True
        