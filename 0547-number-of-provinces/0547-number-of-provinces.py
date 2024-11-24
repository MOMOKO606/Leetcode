class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
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
        
        n = len(isConnected)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    connect(i, j)
        return len(set([parent(i) for i in range(n)]))


        
        