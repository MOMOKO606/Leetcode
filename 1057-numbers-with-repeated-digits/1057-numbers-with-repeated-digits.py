class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        ans, digits, visited = n, list(map(int, list(str(n)))), set()
        n = len(digits)
        for i in range(n - 1): ans -= 9 * perm(9, i)
        for i, digit in enumerate(digits):
            for num in range(i == 0, digit):
                if num in visited: continue
                ans -= perm(9 - i, n - i - 1)
            if digit in visited: return ans
            visited.add(digit)
        return ans - 1


        

        