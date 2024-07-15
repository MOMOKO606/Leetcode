class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return j - i - 1, i + 1, j - 1



        longest, left, right = 1, 0, 0
        for i in range(len(s)):
            length, l, r = getPalindrome(i, i + 1)
            if longest < length: longest, left, right = length, l, r
            length, l, r = getPalindrome(i, i)
            if longest < length: longest, left, right = length, l, r
        return s[left: right + 1]
            
        