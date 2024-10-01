class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n: return False
        return not n & (n - 1)
        