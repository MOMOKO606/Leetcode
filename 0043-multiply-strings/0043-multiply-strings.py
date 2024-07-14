class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        num1, num2, m, n = list(map(int, list(num1))), list(map(int, list(num2))), len(num1), len(num2)
        ans = [0] * (m + n - 1)
        for i in range(m):
            for j in range(n):
                ans[i + j] += num1[i] * num2[j]
        carry = 0
        for k in range(len(ans) - 1, -1, -1):
            ans[k] += carry
            carry = ans[k] // 10
            ans[k] %= 10
        if carry: ans = [carry] + ans
        return "".join(map(str, ans))



        