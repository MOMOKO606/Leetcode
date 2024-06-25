class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(i=0):
            if i == n: 
                self.ans += 1
                return 
            for j in range(n):
                if j in cols or i + j in slashs or i - j in back_slashs: continue
                cols.add(j)
                slashs.add(i + j)
                back_slashs.add(i - j)
                helper(i + 1)
                cols.remove(j)
                slashs.remove(i + j)
                back_slashs.remove(i - j) 
            
        cols, slashs, back_slashs, self.ans = set(), set(), set(), 0
        helper()
        return self.ans

        