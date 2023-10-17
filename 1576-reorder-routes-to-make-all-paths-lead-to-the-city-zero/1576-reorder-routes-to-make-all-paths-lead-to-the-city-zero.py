class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build the graph
        edge = collections.defaultdict(list)
        for u, v in connections:
            edge[u].append((v, 1))
            edge[v].append((u, 0))
        # BFS
        queue, ans = [(-1, 0)], 0
        while queue:
            # u represents the parent node of node v 
            nextQueue = []
            for u, v in queue:
                for next, weight in edge[v]: 
                    if next != u:
                        ans += weight
                        nextQueue.append((v, next))
            queue = nextQueue
        return ans
        