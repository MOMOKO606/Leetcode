class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3: return not s1 and not s2
        if not s1 or not s2: return (s1 or s2) == s3
        ans1, ans2 = False, False
        if s1[-1] == s3[-1]:  
            ans1 = self.isInterleave(s1[:-1], s2, s3[:-1])
        if s2[-1] == s3[-1]:
            ans2 = self.isInterleave(s1, s2[:-1], s3[:-1])
        return ans1 or ans2
        