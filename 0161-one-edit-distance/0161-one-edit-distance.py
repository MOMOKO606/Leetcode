class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t: return False
        if not s: return len(t) == 1
        if not t: return len(s) == 1
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                left = i
                break
            i, j = i + 1, j + 1
        else:
            left = i if i == len(s) else j

        i, j = len(s) - 1, len(t) - 1
        while i >= 0 and j >= 0:
            if s[i] != t[j]:
                right = j if j > i else i
                break
            i, j = i - 1, j - 1
        else:
            right = i if j < 0 else j

        return left >= right

        