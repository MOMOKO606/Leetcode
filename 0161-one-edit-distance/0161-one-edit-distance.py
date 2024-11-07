class Solution:
    @cache
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t: return False
        if s and t and s[-1] == t[-1]:
            return self.isOneEditDistance(s[:-1], t[:-1])
        return s[:-1] == t or s == t[:-1] or s[:-1] == t[:-1]
        