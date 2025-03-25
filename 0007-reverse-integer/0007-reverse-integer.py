class Solution:
    def reverse(self, x: int) -> int:
        negative = 1 if x >= 0 else -1
        ans, x = 0, abs(x)
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        ans *= negative
        return ans if -2 ** 31 <= ans <= 2 ** 31 - 1 else 0


        