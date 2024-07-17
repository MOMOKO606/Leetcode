class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = -1 if dividend * divisor < 0 else 1
        dividend, divisor, ans = abs(dividend), abs(divisor), 0
        while divisor <= dividend:
            divisor_copy, count = divisor, 1
            while divisor_copy <= dividend:
                ans, divisor_copy, count, dividend = ans + count, divisor_copy + divisor_copy, count + count, dividend - divisor_copy
        ans *= negative
        return sorted([ans, -2 ** 31, 2 ** 31 - 1])[1]


        