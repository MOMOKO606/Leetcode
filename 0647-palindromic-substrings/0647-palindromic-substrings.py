class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(i, j):
            count = 0
            while i >= 0 and j < len(s) and i <= j and s[i] == s[j]:
                count, i, j = count + 1, i - 1, j + 1
            return count
        
        ans = 0
        for i in range(len(s)):
            ans += helper(i, i)
            ans += helper(i, i + 1)
        return ans



        