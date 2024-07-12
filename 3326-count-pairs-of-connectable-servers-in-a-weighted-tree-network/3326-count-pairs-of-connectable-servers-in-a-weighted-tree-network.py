class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        def dfsHelper(node, weight, visited):
            if node in visited: return 0
            visited.add(node)
            ans = 1 if not weight % signalSpeed else 0
            for neigbhor in graph[node]:
                ans += dfsHelper(neigbhor, weight + graph[node][neigbhor], visited)
            return ans

        def get_paths_in_differ_directs(node):
            return [dfsHelper(neigbhor, graph[node][neigbhor], set([node])) for neigbhor in graph[node]]

        def get_pairs(nums):
            count = 0
            for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    count += nums[i] * nums[j]
            return count

        # Build the graph
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        
        n, ans = len(edges) + 1, []
        for node in range(n):
            paths = get_paths_in_differ_directs(node)
            pairs = get_pairs(paths)
            ans.append(pairs)
        return ans
        