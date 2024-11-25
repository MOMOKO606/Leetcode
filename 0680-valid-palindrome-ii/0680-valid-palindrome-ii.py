class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(i, j):
            if i >= j: return True
            if s[i] == s[j]: return helper(i + 1, j - 1)
            return s[i + 1: j + 1] == s[i + 1: j + 1][::-1] or s[i: j] == s[i: j][::-1]
        return helper(0, len(s) - 1)
        