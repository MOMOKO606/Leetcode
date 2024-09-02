class Solution:
    @cache
    def numDistinct(self, s: str, t: str) -> int:
        if not t: return 1
        if len(s) < len(t): return 0
        ans = self.numDistinct(s[:-1], t)
        if s[-1] == t[-1]:
            ans += self.numDistinct(s[:-1], t[:-1])
        return ans
        