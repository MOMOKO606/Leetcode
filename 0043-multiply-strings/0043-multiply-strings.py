class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        num1, num2 = list(map(int, list(num1))), list(map(int, list(num2)))
        m, n = len(num1), len(num2)
        digits, carry = [0] * (m + n - 1), 0
        for i in range(m):
            for j in range(n):
                digits[i + j] += num1[i] * num2[j]
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
        if carry: digits = [carry] + digits
        return "".join(map(str, digits))
        