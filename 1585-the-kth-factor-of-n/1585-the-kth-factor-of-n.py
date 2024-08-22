class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors, test1, test2 = [], [], []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i: continue
            test1.append(i)
            if n // i != i:
                factors.append(n // i)
                test2.append(n // i)
            k -= 1
            if not k: return i
        k -= 1
        return factors[::-1][k] if k < len(factors) else -1

        