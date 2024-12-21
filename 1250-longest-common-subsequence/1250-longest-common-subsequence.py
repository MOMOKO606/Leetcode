class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def helper(i, j):
            if i < 0 or j < 0: return 0
            if text1[i] == text2[j]: return 1 + helper(i - 1, j - 1)
            return max(helper(i - 1, j), helper(i, j - 1))
         
        return helper(len(text1) - 1, len(text2) - 1)

        