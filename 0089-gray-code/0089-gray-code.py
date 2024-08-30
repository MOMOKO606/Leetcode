class Solution:
    def grayCode(self, n: int) -> List[int]:
        head, ans = 1, [0]
        for _ in range(n):
            ans += [head + prev for prev in reversed(ans)]
            head <<= 1
        return ans
        