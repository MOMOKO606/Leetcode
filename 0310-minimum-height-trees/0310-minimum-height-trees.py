class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        # Build the graph
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [node for node in graph if len(graph[node]) == 1]
        while leaves:
            next_leaves = set()
            if n <= 2: return leaves
            for leaf in leaves:
                n -= 1
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) < 2: next_leaves.add(neighbor)
            leaves = list(next_leaves)
            
        