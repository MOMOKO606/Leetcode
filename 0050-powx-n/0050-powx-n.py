class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        if n < 0: return 1 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n & 1: return half * half * x
        else: return half * half