class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def parent(i):
            root = i
            while root != p[root]:
                root = p[root]
            while i != p[i]:
                p[i], i = root, p[i]
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj
        
        n = len(isConnected)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if not isConnected[i][j]: continue
                connect(i, j)
        return len({parent(i): i for i in range(n)})
        