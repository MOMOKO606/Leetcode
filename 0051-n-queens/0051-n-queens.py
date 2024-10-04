class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(i=0):
            if i == n: 
                ans.append(seq[:])
                return 
            for j in range(n):
                if j in cols or i + j in slashes or i - j in back_slashes: continue
                cols.add(j)
                slashes.add(i + j)
                back_slashes.add(i - j)
                seq.append(j)
                helper(i + 1)
                seq.pop()
                cols.remove(j)
                slashes.remove(i + j)
                back_slashes.remove(i - j)

        cols, slashes, back_slashes, seq, ans = set(), set(), set(), [], []
        helper()
        return [["." * pos + "Q" + "." * (n - pos - 1) for pos in seq] for seq in ans]
