class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        @cache
        def helper(i, j):
            if i > j: return 0
            ans = 0
            for char in "abcd":
                left = s.find(char, i, j + 1)
                right = s.rfind(char, i, j + 1)
                if left == -1: continue
                ans += helper(left + 1, right - 1) + 2 if left != right else 1
            return ans

        return helper(0, len(s) - 1) % (10 ** 9 + 7)

        