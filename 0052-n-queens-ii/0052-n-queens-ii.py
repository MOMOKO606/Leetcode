class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(i=0):
            if i == n: return 1
            ans = 0
            for j in range(n):
                if j in cols or i - j in backSlash or i + j in slash: continue
                cols.add(j)
                backSlash.add(i - j)
                slash.add(i + j)
                ans += helper(i + 1)
                cols.remove(j)
                backSlash.remove(i - j)
                slash.remove(i + j)
            return ans

        cols, backSlash, slash = set(), set(), set()
        return helper()

        