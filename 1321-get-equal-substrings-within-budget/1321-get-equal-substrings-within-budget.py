class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i, ans = -1, 0
        for j in range(len(s)):
            maxCost -= abs(ord(t[j]) - ord(s[j]))
            while maxCost < 0:
                i += 1
                maxCost += abs(ord(t[i]) - ord(s[i]))
            ans = max(ans, j - i)
        return ans
        