class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(iter=0):
            if iter == len(remain):
                return True
            i, j = remain[iter]
            k = 3 * (i // 3) + j // 3
            for num in rows[i] & cols[j] & blocks[k]:
                board[i][j] = str(num)
                rows[i].remove(num)
                cols[j].remove(num)
                blocks[k].remove(num)
                if helper(iter + 1): return True
                board[i][j] = "."
                rows[i].add(num)
                cols[j].add(num)
                blocks[k].add(num)

        rows = [set([i for i in range(1, 10)]) for _ in range(9)]
        cols = [set([i for i in range(1, 10)]) for _ in range(9)]
        blocks = [set([i for i in range(1, 10)]) for _ in range(9)]
        remain, iter = [], 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": 
                    remain.append([i, j])
                else:
                    k, num = 3 * (i // 3) + j // 3, int(board[i][j])
                    rows[i].remove(num)
                    cols[j].remove(num)
                    blocks[k].remove(num)
        helper()
        return

        
        