class Solution:
    def countDigitOne(self, n: int) -> int:
        digits = []
        while n: digits, n = digits + [n % 10], n // 10
        digits, ans = digits[::-1], 0
        for k, digit in enumerate(digits):
            left, right, p = 0, 0, 1
            for i in range(k): left = left * 10 + digits[i]
            for j in range(k + 1, len(digits)): right, p = right * 10 + digits[j], p * 10
            if digit == 0: ans += left * p
            elif digit == 1: ans += right + 1 + left * p
            else: ans += (left + 1) * p
        return ans

            

        