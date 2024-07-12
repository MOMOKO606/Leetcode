class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        @cache
        def helper(i=0, j=len(s) - 1):
            if i > j: return 0
            ans = 0
            for char in "abcd":
                l, r = s.find(char, i, j + 1), s.rfind(char, i, j + 1)
                if l == -1: continue
                ans = ans + helper(l + 1, r - 1) + 2 if l != r else ans + 1
            return ans
        MOD = 10 ** 9 + 7
        return helper() % MOD 


        