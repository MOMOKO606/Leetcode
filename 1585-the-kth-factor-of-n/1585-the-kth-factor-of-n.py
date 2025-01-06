class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        right = []
        for divisor in range(1, floor(n ** 0.5) + 1):
            if not n % divisor: 
                k -= 1
                if not k: return divisor
                if divisor * divisor != n: right = [n // divisor] + right
        return right[k - 1] if k - 1 < len(right) else -1