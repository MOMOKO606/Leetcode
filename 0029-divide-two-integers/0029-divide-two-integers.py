class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = 1 if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        ans, dividend, divisor = 0, abs(dividend), abs(divisor)
        while dividend >= divisor:
            divisor_copy, factor = divisor, 1
            while dividend >= divisor_copy:
                dividend -= divisor_copy
                ans += factor
                divisor_copy += divisor_copy
                factor += factor
        return sorted([-2 ** 31, 2 ** 31 - 1, ans * negative])[1]
                
