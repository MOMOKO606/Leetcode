from itertools import groupby

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def dfs_helper(node):
            if node in local_visited: return
            local_visited.add(node)
            known.add(node)
            for neighbor in graph[node]:
                dfs_helper(neighbor)

        known = set([0, firstPerson])
        for _, group in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            graph, local_visited = collections.defaultdict(list), set([])
            for u, v, _ in group:
                graph[u].append(v)
                graph[v].append(u)

            for node in graph:
                if node not in known: continue
                dfs_helper(node)
        return list(known)

        