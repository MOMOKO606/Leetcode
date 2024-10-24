class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp = [0] * len(s)
        for j in range(1, len(s)):
            if s[j] == ")":
                if s[j - 1] == "(":
                    dp[j] = dp[j - 2] + 2 if j > 1 else 2
                else:
                    i = j - dp[j - 1] - 1
                    if i >= 0 and s[i] == "(":
                        dp[j] = dp[i - 1] + dp[j - 1] + 2 if i >= 1 else dp[j - 1] + 2
        return max(dp) 
        