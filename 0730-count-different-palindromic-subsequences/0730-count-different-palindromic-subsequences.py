class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        @cache
        def helper(i, j):
            if i > j: return 0
            ans = 0
            for char in "abcd":
                l, r = s.find(char, i, j + 1), s.rfind(char, i, j + 1)
                if l == -1: continue
                if l == r: 
                    ans += 1
                else: 
                    ans += helper(l + 1, r - 1) + 2
            return ans

        MOD = 10 ** 9 + 7
        return helper(0, len(s) - 1) % MOD
