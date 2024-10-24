class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfsHelper(iter=0):
            if iter == len(remain): return True
            i, j = remain[iter]
            k = (i // 3) * 3 + j // 3
            for num in rows[i] & cols[j] & blocks[k]:
                rows[i].remove(num)
                cols[j].remove(num)
                blocks[k].remove(num)
                board[i][j] = str(num)
                if dfsHelper(iter + 1): return True
                rows[i].add(num)
                cols[j].add(num)
                blocks[k].add(num)
                board[i][j] = "."

        
        
        rows = [set([i for i in range(1, 10)]) for _ in range(9)]
        cols = [set([i for i in range(1, 10)]) for _ in range(9)]
        blocks = [set([i for i in range(1, 10)]) for _ in range(9)]
        remain = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".": 
                    remain.append((i, j))
                else:
                    k, num = (i // 3) * 3 + j // 3, int(board[i][j])
                    rows[i].remove(num)
                    cols[j].remove(num)
                    blocks[k].remove(num)
        dfsHelper()

        

        