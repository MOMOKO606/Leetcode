class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(i=0, seq=[]):
            if i == n:
                self.ans.append(seq[:])
                return 
            for j in range(n):
                if j in cols or i + j in slashs or i - j in back_slashs: continue
                cols.add(j)
                slashs.add(i + j)
                back_slashs.add(i - j)
                helper(i + 1, seq + [j])
                cols.remove(j)
                slashs.remove(i + j)
                back_slashs.remove(i - j)

        self.ans, cols, slashs, back_slashs = [], set(), set(), set()
        helper()
        return [["." * pos + "Q" + "." * (n - pos - 1) for pos in seq ]for seq in self.ans ]
        