class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfsHelper(u, v, visited):
            if u not in graph or u in visited: return -1.0
            if u == v: return 1.0
            visited.add(u)
            for neighbor in graph[u]:
                next = dfsHelper(neighbor, v, visited)
                if next != -1:
                    return graph[u][neighbor] * next
            return -1.0
        
        
        # Build the graph
        graph = collections.defaultdict(dict)
        for (u, v), w in zip(equations, values):
            graph[u][v] = w
            graph[v][u] = 1 / w

        ans = []
        for u, v in queries:
            ans.append(dfsHelper(u, v, set()))
        return ans

        

        
        