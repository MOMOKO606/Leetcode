class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial, available, ans = [1] * (n - 1), set([i for i in range(1, n + 1)]), ""
        for i in range(len(factorial) - 2, -1, -1):
            factorial[i] = factorial[i + 1] * (len(factorial) - i)
        for i in range(len(factorial)):
            for j in range(1, n + 1):
                if j not in available: continue
                if factorial[i] >= k:
                    ans += str(j)
                    available.remove(j)
                    break
                else:
                    k -= factorial[i]
        return ans + str(list(available).pop())

        
        