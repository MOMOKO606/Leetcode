class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the graph
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        queue, ans, k, visited = [(src, 0)], inf, k + 2, set([src, 0])
        while queue and k:
            next_queue = []
            for node, price in queue:
                if node == dst: 
                    ans = min(ans, price)
                for neighbor in graph[node]:
                    if price + graph[node][neighbor] > ans or (neighbor, price + graph[node][neighbor]) in visited: continue
                    next_queue.append((neighbor, price + graph[node][neighbor]))
                    visited.add((neighbor, price + graph[node][neighbor]))
                    
            k, queue = k - 1, next_queue
        return ans if ans != inf else -1
        