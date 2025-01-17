class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs_helper(u, v, visited):
            if u not in graph or u in visited: return -1.0
            if u == v: return 1.0
            visited.add(u)
            for neighbor in graph[u]:
                rest = dfs_helper(neighbor, v, visited)
                if rest != -1.0: 
                    return graph[u][neighbor] * rest
            visited.remove(u)
            return -1.0

        # Build the graph
        graph = collections.defaultdict(dict)
        for e, v in zip(equations, values):
            graph[e[0]][e[1]] = v
            graph[e[1]][e[0]] = 1 / v

        ans = []
        for u, v in queries:
            ans.append(dfs_helper(u, v, set()))
        return ans

            