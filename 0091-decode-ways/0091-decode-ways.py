class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if not s: return 1
        ans = 0
        if 1 <= int(s[:1]) <= 9: ans += self.numDecodings(s[1:])
        if 10 <= int(s[:2]) <= 26: ans += self.numDecodings(s[2:])
        return ans
        