class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2: return n
        if n == 2: return 1
        t0, t1, t2 = 0, 1, 1
        for _ in range(n - 2):
            t2, t1, t0 = t0 + t1 + t2, t2, t1
        return t2

        