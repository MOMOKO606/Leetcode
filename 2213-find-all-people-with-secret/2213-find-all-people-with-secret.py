from itertools import groupby


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def dfsHelper(node):
            if node in visited: return
            visited.add(node)
            known.add(node)
            for neighbor in graph[node]:
                dfsHelper(neighbor)

        known = set([0, firstPerson])
        for _, group in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            graph, visited = collections.defaultdict(list), set([])
            for u, v, _ in group:
                graph[u].append(v)
                graph[v].append(u)

            for node in graph.keys():
                if node not in known: continue
                dfsHelper(node)

        return list(known)
                

            

        