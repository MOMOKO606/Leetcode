class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def parent(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                i, p[i] = p[i], root
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj

        p, cables = [i for i in range(n)], 0
        for i, j in connections:
            pi, pj = parent(i), parent(j)
            if pi == pj: cables += 1
            else: connect(i, j)
        unconnected = len(set([parent(i) for i in range(n)])) - 1
        return unconnected if cables >= unconnected else -1

        
            
        