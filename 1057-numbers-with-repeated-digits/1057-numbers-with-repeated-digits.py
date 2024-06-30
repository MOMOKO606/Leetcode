class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        ans, digits, visited = n, list(map(int, list(str(n)))), set([])
        n = len(digits)
        for i in range(1, n):
            ans -= 9 * perm(9, i - 1)
        for i, digit in enumerate(digits):
            for j in range(i == 0, digit):
                if j in visited: continue
                ans -= perm(9 - i, n - i - 1)
            if digit in visited: return ans
            visited.add(digit)
        return ans - 1
    

        