class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            next_num = 0
            while num:
                next_num += num % 10
                num //= 10
            num = next_num
        return num
        