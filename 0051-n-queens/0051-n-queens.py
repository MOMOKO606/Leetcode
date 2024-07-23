class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(i=0, seq=[]):
            if i == n:
                ans.append(seq[:])
                return
            for j in range(n):
                if j in cols or i - j in slash or i + j in back_slash: continue
                cols.add(j)
                slash.add(i - j)
                back_slash.add(i + j)
                helper(i + 1, seq + [j])
                cols.remove(j)
                slash.remove(i - j)
                back_slash.remove(i + j)


        cols, slash, back_slash, ans = set(), set(), set(), []
        helper()
        return [["." * j + "Q" + "." * (n - j - 1) for j in seq] for seq in ans]


        