class Solution:
    def minOperations(self, k: int) -> int:
        ans = inf
        for i in range(1, k + 1):
            ans = min(ans, math.ceil(k / i)+  i - 2)
        return ans


        