class Solution:
    def baseNeg2(self, n: int) -> str:
        if 0 <= n < 2: return str(n)
        if n & 1: return self.baseNeg2(ceil(n / -2)) + "1"
        else: return self.baseNeg2(n // -2) + "0"

        