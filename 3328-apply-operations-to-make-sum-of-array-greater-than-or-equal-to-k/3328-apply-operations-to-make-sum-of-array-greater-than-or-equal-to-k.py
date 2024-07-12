class Solution:
    def minOperations(self, k: int) -> int:
        ans = inf
        for i in range(1, math.ceil(k ** 0.5) + 1):
            ans = min(ans, math.ceil(k / i) - 1 + i - 1)
        return ans


        