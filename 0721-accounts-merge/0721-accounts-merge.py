class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs_helper(i):
            if i in id_visited: return []
            id_visited.add(i)
            emails = []
            for email in accounts[i][1:]:
                if email in email_visited: continue
                email_visited.add(email)
                emails.append(email)
                for neighbor in graph[email]:
                    emails += dfs_helper(neighbor)
            return emails



        # Build the graph
        graph = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                graph[email].append(i)

        id_visited, email_visited, ans = set(), set([]), []
        for i, account in enumerate(accounts):
            if i in id_visited: continue
            name = account[0]
            emails = dfs_helper(i)
            ans.append([name] + sorted(emails))
        return ans


        