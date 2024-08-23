class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3: return [i for i in range(n)]
        # Build the graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = [node for node in range(n) if len(graph[node]) == 1]
        while queue:
            if n < 3: return queue
            next_queue = set()
            for node in queue:
                neighbor, n = graph[node].pop(), n - 1
                graph[neighbor].remove(node)
                if len(graph[neighbor]) < 2:
                    next_queue.add(neighbor)
            queue = list(next_queue)
