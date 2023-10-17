class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build the graph
        edge = collections.defaultdict(list)
        for u, v in connections:
            edge[u].append((v, 1))
            edge[v].append((u, 0))
        # BFS
        queue, ans, visited = [0], 0, set([0])
        while queue:
            nextQueue = []
            for u in queue:
                for v, weight in edge[u]: 
                    if v not in visited:
                        ans += weight
                        visited.add(v)
                        nextQueue.append((v))
            queue = nextQueue
        return ans
        