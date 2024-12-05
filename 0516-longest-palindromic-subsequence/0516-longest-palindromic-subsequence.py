class Solution:
    @cache
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        if s[0] == s[-1]: return self.longestPalindromeSubseq(s[1: -1]) + 2
        else: return max(self.longestPalindromeSubseq(s[:-1]), self.longestPalindromeSubseq(s[1:]))
        