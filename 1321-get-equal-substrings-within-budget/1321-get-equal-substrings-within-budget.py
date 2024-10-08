class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i, ans = -1, -inf
        for j in range(len(s)):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            while maxCost < 0:
                i += 1
                maxCost += abs(ord(s[i]) - ord(t[i]))
            ans = max(ans, j - i)
        return ans
        