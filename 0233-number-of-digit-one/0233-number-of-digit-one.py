class Solution:
    def countDigitOne(self, n: int) -> int:
        digits, ans = [], 0
        while n: digits, n = [n % 10] + digits, n // 10
        for j, digit in enumerate(digits):
            left, right, factor = 0, 0, 1
            for i in range(j):  left = left * 10 + digits[i]
            for i in range(j + 1, len(digits)): right, factor = right * 10 + digits[i], factor * 10
            if digit == 0: ans += left * factor
            elif digit == 1: ans += left * factor + right + 1
            else: ans += (left + 1) * factor
        return ans
        