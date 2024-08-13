class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3: return [i for i in range(n)]
        # Build the graph
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        queue, node_count = [node for node in range(n) if len(graph[node]) == 1], n
        while True:
            if node_count < 3: return queue
            nextQueue = []
            for node in queue:
                node_count -= 1
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                    if len(graph[neighbor]) == 1:
                        nextQueue.append(neighbor)
            queue = nextQueue
        