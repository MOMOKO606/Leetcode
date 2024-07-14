class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = -1 if dividend * divisor < 0 else 1
        ans, dividend, divisor = 0, abs(dividend), abs(divisor)
        while divisor <= dividend:
            copied_divisor, count = divisor, 1
            while copied_divisor <= dividend:
                dividend -= copied_divisor
                ans += count
                count += count
                copied_divisor += copied_divisor
        return sorted([-2 ** 31, ans * negative, 2 ** 31 - 1])[1]