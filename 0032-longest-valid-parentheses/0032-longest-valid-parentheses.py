class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s)):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2 if i > 1 else 2
                else: 
                    j = i - dp[i - 1] - 1
                    if j >= 0 and s[j] == "(":
                        dp[i] = dp[j - 1] + dp[i - 1] + 2 if j > 0 else dp[i - 1] + 2
        return max(dp) if dp else 0
        