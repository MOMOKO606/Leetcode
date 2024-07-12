class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits, ans, visited = [], n, set()
        while n: n, digits = n // 10, digits + [n % 10]
        digits = digits[::-1]
        digits_length = len(digits)
        for i in range(digits_length - 1): ans -= 9 * math.perm(9, i)
        for i, digit in enumerate(digits):
            for j in range(i == 0, digit):
                if j in visited: continue
                ans -= math.perm(9 - i, digits_length - i - 1)
            if digit in visited: return ans
            visited.add(digit)
        return ans - 1
        