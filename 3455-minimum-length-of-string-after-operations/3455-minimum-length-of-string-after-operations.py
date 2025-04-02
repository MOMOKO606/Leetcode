class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        for freq in Counter(s).values():
            if freq & 1: ans += 1
            else: ans += 2
        return ans
        