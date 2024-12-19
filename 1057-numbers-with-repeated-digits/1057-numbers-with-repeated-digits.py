class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        ans, digits, visited = n, [], set()
        while n: digits, n = [n % 10] + digits, n // 10
        digits_length = len(digits)
        for i in range(digits_length - 1):
            ans -= 9 * perm(9, i)
        for i, digit in enumerate(digits):
            for num in range(i == 0, digit):
                if num in visited: continue
                ans -= perm(9 - i, digits_length - i - 1)
            if digit in visited: return ans
            visited.add(digit)
        return ans - 1
        

        
        