class Solution:
    def minOperations(self, k: int) -> int:
        ans = inf
        for i in range(math.ceil(k ** 0.5)):
            ans = min(ans, math.ceil(k / (i + 1)) +  i - 1)
        return ans


        