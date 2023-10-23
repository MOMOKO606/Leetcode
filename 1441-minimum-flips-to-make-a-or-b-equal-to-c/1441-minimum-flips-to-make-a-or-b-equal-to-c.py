class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a > 0 or b > 0 or c > 0:
            aBit, bBit, cBit = a & 1, b & 1, c & 1
            if not cBit: ans += aBit + bBit
            elif not aBit and not bBit: ans += 1
            a, b, c = a >> 1, b >> 1, c >> 1
        return ans
        