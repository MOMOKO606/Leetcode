class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if not s: return 1
        ans = 0
        if int(s[0]) > 0: ans += self.numDecodings(s[1:])
        if 9 < int(s[:2]) < 27: ans += self.numDecodings(s[2:])
        return ans
        