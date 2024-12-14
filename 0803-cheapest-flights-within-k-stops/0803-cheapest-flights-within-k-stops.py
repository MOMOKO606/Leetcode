class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the graph
        graph = collections.defaultdict(dict)
        for u, v, price in flights:
            graph[u][v] = price

        queue, k, ans, visited = [(src, 0)],  k + 1, inf, [inf] * n
        while queue and k:
            next_queue = []
            for node, cur_cost in queue:
                for neighbor in graph[node]:
                    if cur_cost + graph[node][neighbor] > visited[neighbor]: continue
                    visited[neighbor] = cur_cost + graph[node][neighbor]
                    next_queue.append((neighbor, cur_cost + graph[node][neighbor]))
            queue, k = next_queue, k - 1
        return visited[dst] if visited[dst] != inf else -1


        