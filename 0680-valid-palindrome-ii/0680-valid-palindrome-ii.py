class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return s[i + 1: j + 1] == s[i + 1: j + 1][::-1] or s[i: j] == s[i: j][::-1]
            i, j = i + 1, j - 1
        return True
        