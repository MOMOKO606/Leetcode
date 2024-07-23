class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(i=0):
            if i == n: return 1
            ans = 0
            for j in range(n):
                if j in cols or i - j in slash or i + j in back_slash: continue
                cols.add(j)
                slash.add(i - j)
                back_slash.add(i + j)
                ans += helper(i + 1)
                cols.remove(j)
                slash.remove(i - j)
                back_slash.remove(i + j)
            return ans
        cols, slash, back_slash = set(), set(), set()
        return helper()
        