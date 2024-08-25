class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i + 1: j]
        
        ans = ""
        for i in range(len(s)):
            ans = max(ans, helper(i, i), helper(i, i + 1), key=len)
        return ans

