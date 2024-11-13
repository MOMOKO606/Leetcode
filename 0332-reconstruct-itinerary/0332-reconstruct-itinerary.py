class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfsHelper(node="JFK"):
            while graph[node]:
                neighbor = graph[node].pop(0)
                dfsHelper(neighbor)
            ans.append(node)

        # Build the graph
        graph, ans = collections.defaultdict(list), []
        for u, v in sorted(tickets):
            graph[u].append(v)
        dfsHelper()
        return ans[::-1]

        
        