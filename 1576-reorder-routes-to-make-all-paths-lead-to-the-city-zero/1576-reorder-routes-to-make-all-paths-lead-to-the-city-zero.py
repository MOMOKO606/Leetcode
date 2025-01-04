class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(dict)
        # Build the graph
        for u, v in connections:
            graph[u][v] = 1
            graph[v][u] = 0
        
        queue, ans, visited = [0], 0, set([0])
        while queue:
            next_queue = []
            for node in queue:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_queue.append(neighbor)
                        ans += graph[node][neighbor]
            queue = next_queue
        return ans


        