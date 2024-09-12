class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans, one = [0], 1
        for _ in range(n):
            ans += [one + digit for digit in reversed(ans)]
            one <<= 1
        return ans

        