class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
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
        
        p, ans = [i for i in range(n)], []
        for u, v, _ in edges:
            connect(u, v)
            
        root2weight = {parent(i): -1 for i in range(n)}
        for u, v, w in edges:
            root2weight[parent(u)] &= w

        for u, v in query:
            pu, pv = parent(u), parent(v)
            if pu == pv: ans.append(root2weight[pu])
            else: ans.append(-1)

        return ans
        
        