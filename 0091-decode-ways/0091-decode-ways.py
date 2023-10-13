class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if not s: return 1
        ans = 0
        if 0 < int(s[0]) < 10: ans += self.numDecodings(s[1:])
        if 9 < int(s[:2]) < 27: ans += self.numDecodings(s[2:])
        return ans
        