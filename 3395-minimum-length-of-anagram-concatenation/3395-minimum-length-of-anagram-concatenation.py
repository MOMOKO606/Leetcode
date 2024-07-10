class Solution:
    def minAnagramLength(self, s: str) -> int:
        for l in range(1, len(s)):
            if len(s) % l: continue
            target = sorted(s[:l])
            for i in range(l, len(s), l):
                if sorted(s[i: i + l]) != target:
                    break
            else: return l
        return len(s)
        