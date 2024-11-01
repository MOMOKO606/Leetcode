class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3: return not s1 and not s2
        possible1, possible2 = False, False
        if s1 and s3[-1] == s1[-1]: possible1 = self.isInterleave(s1[:-1], s2, s3[:-1])
        if s2 and s3[-1] == s2[-1]: possible2 = self.isInterleave(s1, s2[:-1], s3[:-1])
        return possible1 or possible2

        