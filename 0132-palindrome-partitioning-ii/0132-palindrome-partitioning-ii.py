class Solution:
    @cache
    def minCut(self, s: str) -> int:
        if not s: return -1
        ans = inf
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                ans = min(ans, 1 + self.minCut(s[i:]))
        return ans




        
        