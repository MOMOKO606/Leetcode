class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        from collections import defaultdict
        person = defaultdict(int)
        for x, y, z in transactions:
            person[x] -= z
            person[y] += z
        # 账号
        accounts = list(person.values())
       
        res = float("inf")

        def dfs(i, cnt):
            nonlocal res
            # 全局变量退出递归
            if cnt >= res: return 
            # 账号为0不考虑
            while i < len(accounts) and accounts[i] == 0: i += 1
            # 遍历完
            if i == len(accounts):
                res = min(res, cnt)
                return
            for j in range(i + 1, len(accounts)):
                if accounts[i] * accounts[j] < 0:
                    accounts[j] += accounts[i]
                    dfs(i + 1, cnt + 1)
                    accounts[j] -= accounts[i]

        dfs(0, 0)
        return res
        