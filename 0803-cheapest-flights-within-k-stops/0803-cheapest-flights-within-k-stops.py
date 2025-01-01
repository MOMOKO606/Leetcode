class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the graph
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        queue, k, visited = [(src, 0)], k + 1, [inf] * n
        while queue and k:
            next_queue = []
            for node, cur_cost in queue:
                for neighbor in graph[node]:
                    if cur_cost + graph[node][neighbor] > visited[neighbor]: continue
                    visited[neighbor] = cur_cost + graph[node][neighbor]
                    next_queue.append((neighbor, cur_cost + graph[node][neighbor]))
                    
            k, queue = k - 1, next_queue
        return visited[dst] if visited[dst] != inf else -1
        