class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10:
            digits = 0
            while num:
                digits += num % 10
                num //= 10
            num = digits
        return num

        