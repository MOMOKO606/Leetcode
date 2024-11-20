class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s, i, j, ans = sorted(g), sorted(s), 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]: i, j, ans = i + 1, j + 1, ans + 1
            else: j += 1
        return ans

        