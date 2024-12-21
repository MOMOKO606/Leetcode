class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def parent(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                p[i], i = root, p[i]
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj

        p, cables = [i for i in range(n)], 0
        for u, v in connections:
            pu, pv = parent(u), parent(v)
            if pu == pv: cables += 1
            else: connect(u, v)
        ans = len(set([parent(i) for i in range(n)])) - 1
        
        return ans if cables >= ans else -1
        