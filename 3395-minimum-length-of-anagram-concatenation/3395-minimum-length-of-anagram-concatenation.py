class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for l in range(1, n + 1):
            if n % l: continue
            target = Counter(s[:l])
            for j in range(l, n, l):
                if Counter(s[j: j + l]) != target: break
            else:
                return l
        