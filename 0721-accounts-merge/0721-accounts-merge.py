class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfsHelper(i):
            if i in i_visited: return []
            i_visited.add(i)
            emails = []
            for email in accounts[i][1:]:
                if email in email_visited: continue
                email_visited.add(email)
                emails.append(email)
                for neighbor in graph[email]:
                    emails += dfsHelper(neighbor)
            return emails
        
        
        
        graph = collections.defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                graph[email].add(i)

        ans, i_visited, email_visited = [], set(), set()
        for i, account in enumerate(accounts):
            if i in i_visited: continue
            ans.append([account[0]] + sorted(dfsHelper(i)))
        return ans
           


        