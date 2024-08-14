class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfsHelper(node):
            neighbors = graph[node]
            while neighbors:
                dfsHelper(neighbors.pop(0))
            ans.append(node)

        # Build the graph
        graph = collections.defaultdict(list)
        for u, v in sorted(tickets):
            graph[u].append(v)
        
        
        ans = []
        dfsHelper("JFK")
        return ans[::-1]
        