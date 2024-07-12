class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 1 or n == 0: return str(n)
        if n & 1: return self.baseNeg2(math.ceil(n / -2)) + "1" 
        else: return self.baseNeg2(n // -2) + "0"
        