class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfsHelper(i, j):
            if not (0 <= i < n and 0 <= j < n and isConnected[i][j]): return
            isConnected[i][j] = 0
            for di in range(n):
                dfsHelper(di, j)
            for dj in range(n):
                dfsHelper(i, dj)


        n, ans = len(isConnected), 0
        for k in range(n):
            for i in range(n):
                if isConnected[i][k]: ans += 1
                dfsHelper(i, k)
            for j in range(n):
                if isConnected[k][j]: ans += 1
                dfsHelper(k, j)
        return ans

        