class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans, head = [0], 1
        for _ in range(n):
            ans += [head + prev for prev in reversed(ans)]
            head <<= 1
        return ans
        