class Solution:
    def reverse(self, x: int) -> int:
        if not x: return x
        negative = 1 if x > 0 else -1
        x, digits, ans = abs(x), [], 0
        while x:
            digits.append(x % 10)
            x //= 10
        while not digits[0]:
            digits.pop(0)
        for digit in digits:
            ans = ans * 10 + digit
        ans = ans * negative
        return ans if -2 ** 31 <= ans <= 2 ** 31 - 1 else 0
        

        