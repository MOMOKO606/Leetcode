class Solution:
    def convert(self, s: str, numRows: int) -> str:
        table, deque, j = [[0] * len(s) for _ in range(numRows)], collections.deque(list(s)), 0
        while deque:
            # Going down
            for i in range(numRows):
                if not deque: break
                table[i][j] = deque.popleft()
            
            # Going up
            j += 1
            for i in range(numRows - 2, 0, -1):
                if not deque: break
                table[i][j], j = deque.popleft(), j + 1

        # Print the table
        return "".join([table[i][j] for i in range(numRows) for j in range(len(s)) if table[i][j]])

            
        