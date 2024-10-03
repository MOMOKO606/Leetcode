class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfsHelper(node="JFK"):
            while graph[node]:
                neighbor = graph[node].pop(0)
                dfsHelper(neighbor)
            ans.append(node)

        tickets, graph, ans = sorted(tickets), collections.defaultdict(list), []
        # Build the graph
        for u, v in tickets:
            graph[u].append(v)
        dfsHelper()
        return ans[::-1]
        