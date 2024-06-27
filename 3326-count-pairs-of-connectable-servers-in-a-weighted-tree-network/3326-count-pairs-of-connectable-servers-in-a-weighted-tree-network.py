class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        def dfsHelper(cur_node, cur_weight, visited):
            if cur_node in visited: return 0
            ans = 1 if not cur_weight % signalSpeed else 0
            visited.add(cur_node)
            for neighbor in graph[cur_node]:
                ans += dfsHelper(neighbor, cur_weight + graph[cur_node][neighbor], visited)
            return ans

        def getPaths(node):
            paths = []
            for neighbor in graph[node]:
                paths.append(dfsHelper(neighbor, graph[node][neighbor], set([node])))
            return paths
        
        # Build the graph
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        ans = []
        for node in range(len(edges) + 1):
            path, count = getPaths(node), 0
            for i in range(len(path) - 1):
                for j in range(i + 1, len(path)):
                    count += path[i] * path[j]
            ans.append(count)
        return ans





        