class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for j in range(1, len(s)):
            l = len(ans)
            if s[j - l: j + 1] == s[j - l: j + 1][::-1]:
                ans = max(ans, s[j - l: j + 1], key=len)
            if s[j - l - 1: j + 1] == s[j - l - 1: j + 1][::-1]:
                ans = max(ans, s[j - l - 1: j + 1], key=len)
        return ans

        