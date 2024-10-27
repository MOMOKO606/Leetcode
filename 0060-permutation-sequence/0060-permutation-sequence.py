class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        available, ans = set([i for i in range(1, n + 1)]), ""
        
        factorial = [i for i in range(1, n)]
        for i in range(2, len(factorial)):
            factorial[i] *= factorial[i - 1]
        factorial.reverse()

        for i in range(n - 1):
            for j in range(1, n + 1):
                if j not in available: continue
                if k > factorial[i]:
                    k -= factorial[i]
                else:
                    ans = ans + str(j)
                    available.remove(j)
                    break
        return ans + str(list(available).pop())
        

        