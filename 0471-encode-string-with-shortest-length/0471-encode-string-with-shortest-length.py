class Solution:
    @cache
    def encode(self, s: str) -> str:
        l = (s + s).find(s, 1, -1)
        ans = str(len(s) // l) + "[" + self.encode(s[:l]) + "]" if l != -1 else s
        for i in range(1, len(s)):
            ans = min(ans, self.encode(s[:i]) + self.encode(s[i:]), key=len)
        return ans
