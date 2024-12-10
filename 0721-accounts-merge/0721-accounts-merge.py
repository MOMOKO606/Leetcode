class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def parent(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                i, p[i] = p[i], root
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj

        p = [i for i in range(len(accounts))]

        email_to_account, root_to_email = {}, collections.defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    connect(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        for i, account in enumerate(accounts):
            pi = parent(i)
            for email in account[1:]:
                root_to_email[pi].add(email)

        return [[accounts[i][0]] + sorted(list(emails)) for i, emails in root_to_email.items()]

        

        


        