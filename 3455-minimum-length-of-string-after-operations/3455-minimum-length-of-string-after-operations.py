class Solution:
    def minimumLength(self, s: str) -> int:
        freqs, ans = Counter(s).values(), 0
        for freq in freqs:
            if freq & 1: ans += 1
            else: ans += 2
        return ans