class Solution:
    def grayCode(self, n: int) -> List[int]:
        one, ans = 1, [0]
        for _ in range(n):
            ans += [one + num for num in reversed(ans)]
            one <<= 1
        return ans
        