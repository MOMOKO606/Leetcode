class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(i, j):
            while i >= 0 and j < len(s):
                if s[i] != s[j]: return s[i + 1: j]
                i, j = i - 1, j + 1
            return s[i + 1: j] 

        ans = ""
        for i in range(len(s)):
            ans = max(ans, isPalindrome(i, i), key=len)
            ans = max(ans, isPalindrome(i, i + 1), key=len)
        return ans 
