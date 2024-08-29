class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3: return [i for i in range(n)]
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = [node for node in graph if len(graph[node]) < 2]
        while queue:
            if n < 3: return queue
            next_queue = set()
            for node in queue:
                n -= 1
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                    if len(graph[neighbor]) < 2:
                        next_queue.add(neighbor)
            queue = list(next_queue)
                

        