class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i, ans = 0, 0
        for j, char in enumerate(s):
            maxCost -= abs(ord(s[j]) - ord(t[j]))
            while maxCost < 0:
                maxCost += abs(ord(s[i]) - ord(t[i]))
                i += 1
            ans = max(ans, j - i + 1)
        return ans

        