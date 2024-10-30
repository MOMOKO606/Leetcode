class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 1: return s1 == s2
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:-i], s2[i:]) and self.isScramble(s1[-i:], s2[:i])):
                return True
        return False
        