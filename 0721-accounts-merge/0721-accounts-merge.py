class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def parent(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                p[i], i = root, p[i]
            return root

        def connect(i, j):
            pi, pj = parent(i), parent(j)
            p[pi] = pj
        
        p, email_to_id, id_to_email = [i for i in range(len(accounts))], {}, collections.defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    connect(email_to_id[email], i)
                else:
                    email_to_id[email] = i

        for i, account in enumerate(accounts):
            pi = parent(i)
            for email in account[1:]:
                id_to_email[pi].add(email)
        return [[accounts[i][0]] + sorted(emails) for i, emails in id_to_email.items()]        




        