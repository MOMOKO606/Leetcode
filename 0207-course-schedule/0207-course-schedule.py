class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph
        graph, indegs = collections.defaultdict(list), {i: 0 for i in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u)
            indegs[u] += 1

        queue = [node for node in indegs if not indegs[node]]
        while queue:
            nextQueue = []
            for node in queue:
                numCourses -= 1
                for neighbor in graph[node]:
                    indegs[neighbor] -= 1
                    if not indegs[neighbor]:
                        nextQueue.append(neighbor)
            queue = nextQueue
        return not numCourses
                        
            
        