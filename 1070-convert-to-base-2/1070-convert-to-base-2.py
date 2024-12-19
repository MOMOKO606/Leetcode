class Solution:
    def baseNeg2(self, n: int) -> str:
        ans = ""
        while n != 1 and n != 0:
            if n & 1: ans, n = "1" + ans, ceil(n / -2)
            else: ans, n = "0" + ans, n // -2
        return str(n) + ans
        