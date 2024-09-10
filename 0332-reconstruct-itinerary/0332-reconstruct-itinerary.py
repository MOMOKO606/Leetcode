class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfsHelper(node):
            while graph[node]:
                dfsHelper(graph[node].pop(0))
            self.ans.append(node)


        # Build the graph
        graph, tickets = collections.defaultdict(list), sorted(tickets)
        for u, v in tickets:
            graph[u].append(v)
        
        self.ans = []
        dfsHelper("JFK")
        return self.ans[::-1]



        