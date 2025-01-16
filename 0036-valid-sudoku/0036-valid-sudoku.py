class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set([i for i in range(1, 10)]) for _ in range(9)]
        cols = [set([i for i in range(1, 10)]) for _ in range(9)]
        blocks = [set([i for i in range(1, 10)]) for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue
                k, num = (i // 3) * 3 + j // 3, int(board[i][j])
                if not (num in rows[i] and num in cols[j] and num in blocks[k]): return False
                rows[i].remove(num)
                cols[j].remove(num)
                blocks[k].remove(num)
        return True