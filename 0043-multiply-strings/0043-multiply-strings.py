class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        m, n = len(num1), len(num2)
        ans, carry = [0] * (m + n - 1), 0
        for i in range(m):
            for j in range(n):
                ans[i + j] += int(num1[i]) * int(num2[j])
        for i in range(len(ans) - 1, -1, -1):
            ans[i] += carry
            carry = ans[i] // 10
            ans[i] %= 10
        if carry: ans = [carry] + ans
        return "".join(map(str, ans))        