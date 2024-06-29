class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        def dfsHelper(cur_node, weight, visited):
            if cur_node in visited: return 0
            visited.add(cur_node)
            ans = 1 if not weight % signalSpeed else 0
            for neighbor in graph[cur_node]:
                ans += dfsHelper(neighbor, weight + graph[cur_node][neighbor], visited)
            return ans
        
        def get_paths_in_diff_directs(node):
            paths = []
            for neighbor in graph[node]:
                paths.append(dfsHelper(neighbor, graph[node][neighbor], set([node])))
            return paths

        def get_result(paths):
            count = 0
            for i in range(len(paths) - 1):
                for j in range(i + 1, len(paths)):
                    count += paths[i] * paths[j]
            return count

        # Build the graph
        graph, n = collections.defaultdict(dict), len(edges) + 1
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        ans = []
        for i in range(n):
            paths = get_paths_in_diff_directs(i)
            ans.append(get_result(paths))
        return ans
        