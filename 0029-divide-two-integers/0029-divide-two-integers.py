class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor, ans = abs(dividend), abs(divisor), 0
        while divisor <= dividend:
            factor, copy_divisor = 1, divisor
            while copy_divisor <= dividend:
                ans += factor
                dividend -= copy_divisor
                copy_divisor += copy_divisor
                factor += factor
        return sorted([-2 ** 31, ans * negative, 2 ** 31 - 1])[1]
        