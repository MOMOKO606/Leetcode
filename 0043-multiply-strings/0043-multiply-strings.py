class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        num1, num2 = list(map(int, list(num1[::-1]))), list(map(int, list(num2[::-1])))
        m, n = len(num1), len(num2)
        ans = [0] * (m + n)
        for i in range(m):
            for j in range(n):
                ans[i + j] += num1[i] * num2[j]
        
        carry = 0
        for i in range(len(ans)):
            ans[i] += carry
            carry = ans[i] // 10
            ans[i] %= 10
        if not ans[-1]: ans.pop()
        ans = ans[::-1]
        return "".join(map(str, ans))
