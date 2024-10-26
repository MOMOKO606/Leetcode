class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(i=0):
            if i == n: 
                ans.append(seq[:])
                return
            for j in range(n):
                if j in cols or i + j in backSlash or i - j in slash: continue
                cols.add(j)
                backSlash.add(i + j)
                slash.add(i - j)
                seq.append(j)
                helper(i + 1)
                cols.remove(j)
                backSlash.remove(i + j)
                slash.remove(i - j)
                seq.pop()

        cols, backSlash, slash, seq, ans = set(), set(), set(), [], []
        helper()
        return [["." * pos + "Q" + "." * (n - pos - 1) for pos in seq] for seq in ans]
        
        