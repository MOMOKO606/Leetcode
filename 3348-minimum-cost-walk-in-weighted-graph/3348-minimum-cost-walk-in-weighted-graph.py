class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
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

        p = [i for i in range(n)]
        for i, j, _ in edges:
            connect(i, j)

        roots = {parent(i): -1 for i in range(n)}
        for i, j, w in edges:
            pi = parent(i)
            roots[pi] = roots[pi] & w

        ans = []
        for i, j in query:
            pi, pj = parent(i), parent(j)
            if pi != pj: ans.append(-1)
            else: ans.append(roots[pi])
        return ans


        