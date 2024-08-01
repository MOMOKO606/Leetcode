class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        f1, f2 = 1, 2
        for _ in range(n - 2):
            f2, f1 = f1 + f2, f2
        return f2
        