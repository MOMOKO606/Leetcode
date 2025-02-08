class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for l in range(1, n + 1):
            if n % l: continue
            target = Counter(s[:l])
            for i in range(l, n, l):
                if Counter(s[i: i + l]) != target: break
            else: return l



        