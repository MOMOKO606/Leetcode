class Solution:
    def countDigitOne(self, n: int) -> int:
        digits, ans = [], 0
        while n: digits, n = digits + [n % 10], n // 10
        digits = digits[::-1]
        for k in range(len(digits)):
            left, right, p = 0, 0, 1
            for i in range(k): left = left * 10 + digits[i] 
            for j in range(k + 1, len(digits)): right, p = right * 10 + digits[j], p * 10 
            digit = digits[k]
            if digit == 0: ans += left * p
            elif digit == 1: ans += left * p + right + 1
            else: ans += (left + 1) * p
        return ans

        