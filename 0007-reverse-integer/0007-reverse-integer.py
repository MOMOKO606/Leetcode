class Solution:
    def reverse(self, x: int) -> int:
        sign, digits, ans = -1 if x < 0 else 1, [], 0
        x = abs(x)
        while x:
            digits.append(x % 10)
            x //= 10
        for digit in digits:
            ans = ans * 10 + digit
        return sign * ans if -2 ** 31 <= sign * ans <= 2 ** 31 - 1 else 0
        

        