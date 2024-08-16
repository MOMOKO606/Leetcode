class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) < k: return 0
        freqs = Counter(s)
        for i, char in enumerate(s):
            if freqs[char] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i + 1:], k)
                break
        else:
            return len(s)
        return max(left, right)
        