class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def helper(i, j):
            if i > j: return 0
            if i == j: return 1
            if s[i] == s[j]:
                return helper(i + 1, j - 1) + 2
            return max(helper(i + 1, j), helper(i, j - 1))
        return helper(0, len(s) - 1)
        