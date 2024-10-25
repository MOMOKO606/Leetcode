class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # edge case
        if num1 == "0" or num2 == "0": return "0"
        ans = [0] * (len(num1) + len(num2) - 1)
        for i in range(len(num2) - 1, -1, -1):
            for j in range(len(num1) - 1, -1, -1):
                ans[i + j] += int(num1[j]) * int(num2[i])
        carry = 0
        for j in range(len(ans) - 1, -1, -1):
            ans[j] += carry
            carry = ans[j] // 10
            ans[j] = str(ans[j] % 10)
        if carry: ans = [str(carry)] + ans
        return "".join(ans)
            

        