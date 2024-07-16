class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if not s: return p[-1] == "*" and self.isMatch(s, p[:-2])
        if s[-1] == p[-1] or p[-1] == ".": return self.isMatch(s[:-1], p[:-1])
        if p[-1] == "*":
            return self.isMatch(s, p[:-2]) or (self.isMatch(s[:-1], p) and (p[-2] == s[-1] or p[-2] == "."))
        return False
        