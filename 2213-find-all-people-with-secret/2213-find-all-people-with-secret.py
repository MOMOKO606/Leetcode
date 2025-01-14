from itertools import groupby


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def parent(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                p[i], i = root, p[i]
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj

        p = [i for i in range(n)]
        connect(0, firstPerson)
        for _, group in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            visited = set([])
            for u, v, _ in group:
                connect(u, v)
                visited.add(u)
                visited.add(v)
            for node in visited:
                if parent(node) != parent(0):
                    p[node] = node
        return [i for i in range(n) if parent(i) == parent(0)]
        