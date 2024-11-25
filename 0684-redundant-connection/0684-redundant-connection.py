class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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

        p = [i for i in range(len(edges) + 1)]
        for u, v in edges:
            pu, pv = parent(u), parent(v)
            if pu == pv: return [u, v]
            connect(u, v)

        