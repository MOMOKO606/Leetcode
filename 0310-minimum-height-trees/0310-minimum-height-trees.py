class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build the graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = [node for node in graph if len(graph[node]) < 2]
        while queue:
            nextQueue = set()
            if len(queue) < 3 and len(queue) == n: return queue
            for node in queue:
                n -= 1
                for neighbor in graph[node]:
                    graph[neighbor].remove(node)
                    if len(graph[neighbor]) < 2:
                        nextQueue.add(neighbor)
            queue = list(nextQueue)
        return [0]

        