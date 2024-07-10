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
        roots = {parent(i): -1 for i in range(n)}
        for u, v, w in edges:
            connect(u, v)
            
        for u, v, w in edges:
            roots[parent(u)] &= w
        
        ans = []
        for u, v in query:
            pu, pv = parent(u), parent(v)
            if pu != pv: ans.append(-1)
            else: ans.append(roots[pu])
        return ans

            



        
            

   
        