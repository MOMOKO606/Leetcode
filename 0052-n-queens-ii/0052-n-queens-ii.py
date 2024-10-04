class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(i=0):
            if i == n: return 1
            ans = 0
            for j in range(n):
                if j in cols or i + j in back_slashes or i - j in slashes: continue
                cols.add(j)
                back_slashes.add(i + j)
                slashes.add(i - j)
                ans += helper(i + 1)
                cols.remove(j)
                back_slashes.remove(i + j)
                slashes.remove(i - j)
            return ans

        cols, slashes, back_slashes  = set(), set(), set()
        return helper()
        
        