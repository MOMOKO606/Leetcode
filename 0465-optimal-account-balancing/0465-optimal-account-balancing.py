class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        mm = collections.defaultdict(int)
        for a,b,m in transactions:
            mm[a] = mm.get(a,0) - m
            mm[b] = mm.get(b,0) + m
        debts = list(mm.values())
        n = len(debts)
        def dfs(pos):
            while pos < n and debts[pos] == 0:
                pos += 1
            if pos == n:
                return 0
            r = float('inf')
            for i in range(pos+1, n):
                if debts[i]*debts[pos] < 0:
                    debts[i] += debts[pos]
                    r= min(r,1+dfs(pos+1))
                    debts[i] -= debts[pos]
            return r
        return dfs(0)
        