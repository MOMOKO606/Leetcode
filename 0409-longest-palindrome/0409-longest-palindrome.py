class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans, has_odd = 0, 0
        for freq in Counter(s).values():
            if not freq & 1: 
                ans += freq
            else: 
                ans += freq - 1
                has_odd = 1
        return ans + has_odd

        