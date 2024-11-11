class Solution:
    def addDigits(self, num: int) -> int:
        if not num: return 0
        digits = []
        while num: digits, num = digits + [num % 10], num // 10

        while len(digits) > 1:
            num = sum([digit for digit in digits])
            digits = []
            while num: digits, num = digits + [num % 10], num // 10
        return digits[0]
        