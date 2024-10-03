class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfsHelper(iter=0):
            if iter == len(remains): return True
            i, j = remains[iter]
            k = (i // 3) * 3 + j // 3
            for num in rows[i] & cols[j] & blocks[k]:
                board[i][j] = str(num)
                rows[i].remove(num)
                cols[j].remove(num)
                blocks[k].remove(num)
                if dfsHelper(iter + 1):
                    return True
                board[i][j] = "."
                rows[i].add(num)
                cols[j].add(num)
                blocks[k].add(num)


        rows = [set([i for i in range(1, 10)]) for _ in range(9)]
        cols = [set([i for i in range(1, 10)]) for _ in range(9)]
        blocks = [set([i for i in range(1, 10)]) for _ in range(9)]
        remains, iter = [], 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": 
                    remains.append([i, j])
                else:
                    num, k = int(board[i][j]), (i // 3) * 3 + j // 3
                    rows[i].remove(num)
                    cols[j].remove(num)
                    blocks[k].remove(num)
        dfsHelper()

        
                

                

        