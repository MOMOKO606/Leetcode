class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfsHelper(node):
            if node in visited: return visited[node]
            visited[node] = True
            for neighbor in graph[node]:
                if dfsHelper(neighbor): return True
            visited[node] = False
            ans.append(node)
        
        
        # Build the graph
        graph, ans, visited = collections.defaultdict(list), [], {}
        for u, v in prerequisites:
            graph[v].append(u)

        for node in range(numCourses):
            if dfsHelper(node): return []
        return ans[::-1]
        
        