class Solution:
    def countDigitOne(self, n: int) -> int:
        digits, ans = [], 0
        while n: digits, n = [n % 10] + digits, n // 10
        for i, digit in enumerate(digits):
            left, right, p = 0, 0, 1
            for j in range(i): left = left * 10 + digits[j]
            for j in range(i + 1, len(digits)): right, p = right * 10 + digits[j], p * 10
            if digit == 0: ans += left * p
            elif digit == 1: ans += left * p + right + 1
            else: ans += (left + 1) * p
        return ans

        
        