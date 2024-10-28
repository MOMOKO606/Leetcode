class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, carry, ans = max(len(a), len(b)), 0, []
        a, b = list(map(int, list(a))), list(map(int, list(b)))
        if len(a) < n: a = [0] * (n - len(a)) + a
        if len(b) < n: b = [0] * (n - len(b)) + b
        for i in range(n - 1, -1, -1):
            carry += a[i] + b[i]
            ans = [str(carry % 2)] + ans
            carry //= 2
        if carry: ans = [str(carry)] + ans
        return "".join(ans)

        
        