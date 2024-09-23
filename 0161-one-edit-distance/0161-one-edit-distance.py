class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t: return False
        if not s: return not t[:-1]
        if not t: return not s[:-1]
        if s[-1] == t[-1]: 
            return self.isOneEditDistance(s[:-1], t[:-1])
        return s == t[:-1] or s[:-1] == t or s[:-1] == t[:-1]

        