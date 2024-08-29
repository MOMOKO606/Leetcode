class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfsHelper(node):
            while graph[node]:
                neighbor = graph[node].pop(0)
                dfsHelper(neighbor)
            ans.append(node)

        # Build the graph
        graph, tickets = collections.defaultdict(list), sorted(tickets)
        for u, v in tickets:
            graph[u].append(v)

        ans = []
        dfsHelper("JFK")
        return ans[::-1]
        