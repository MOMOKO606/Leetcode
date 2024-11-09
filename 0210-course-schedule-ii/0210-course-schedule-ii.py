class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the graph
        graph, indegs = collections.defaultdict(list), {i: 0 for i in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u)
            indegs[u] += 1
        queue, ans = [node for node in indegs if not indegs[node]], []
        while queue:
            nextQueue = []
            for node in queue:
                ans.append(node)
                numCourses -= 1
                for neighbor in graph[node]:
                    indegs[neighbor] -= 1
                    if not indegs[neighbor]: nextQueue.append(neighbor)
            queue = nextQueue
        return ans if not numCourses else []
            
        