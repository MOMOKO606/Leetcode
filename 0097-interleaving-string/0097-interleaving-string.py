class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3: return not s1 and not s2
        if not s1: return s2 == s3
        if not s2: return s1 == s3
        l = self.isInterleave(s1[:-1], s2, s3[:-1]) if s1[-1] == s3[-1] else False
        r = self.isInterleave(s1, s2[:-1], s3[:-1]) if s2[-1] == s3[-1] else False
        return l or r
        