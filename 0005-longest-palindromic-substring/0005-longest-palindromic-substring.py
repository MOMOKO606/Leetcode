class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromeLenght(i, j):
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i + 1: j]
        
        ans = ""
        for i in range(len(s)):
            ans = max(ans, palindromeLenght(i, i), key=len)
            ans = max(ans, palindromeLenght(i, i + 1), key=len)
        return ans


        