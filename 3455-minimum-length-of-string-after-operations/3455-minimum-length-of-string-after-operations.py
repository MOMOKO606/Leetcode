class Solution:
    def minimumLength(self, s: str) -> int:
        ans = len(s)
        for freq in Counter(s).values():
            if freq > 2:
                if freq & 1: ans -= freq - 1
                else: ans -= freq - 2
        return ans

        