class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits, ans, visited = [], n, set([])
        while n: digits, n = digits + [n % 10], n // 10        
        digits, n = digits[::-1], len(digits)
        for i in range(n - 1): ans -= 9 * perm(9, i)
        for i, digit in enumerate(digits):
            for j in range(i == 0, digit):
                if j in visited: continue
                ans -= perm(9 - i, n - i - 1)
            if digit in visited: return ans
            visited.add(digit)
        return ans - 1

