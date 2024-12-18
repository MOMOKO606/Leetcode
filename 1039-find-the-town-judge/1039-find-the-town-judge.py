class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegs, outdegs = collections.defaultdict(int), collections.defaultdict(int)
        for u, v in trust:
            indegs[v] = indegs.get(v, 0) + 1
            outdegs[u] = outdegs.get(u, 0) + 1

        for node in range(1, n + 1):
            if indegs[node] == n - 1 and outdegs[node] == 0: return node
        return -1 
        