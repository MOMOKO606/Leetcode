class Solution:
    def minAnagramLength(self, s: str) -> int:
        for l in range(1, len(s) + 1):
            if len(s) % l: continue
            target = Counter(s[: l])
            for i in range(l, len(s), l):
                if Counter(s[i: i + l]) != target: break
            else:
                return l
        