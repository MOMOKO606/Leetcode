class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for j in range(1, len(s)):
            i = j - len(ans)
            if i >= 0 and s[i: j + 1] == s[i: j + 1][::-1]:
                ans = s[i: j + 1]
            i = j - len(ans) - 1
            if i >= 0 and s[i: j + 1] == s[i: j + 1][::-1]:
                ans = s[i: j + 1]
        return ans


        