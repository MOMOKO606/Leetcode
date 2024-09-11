class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        freqs = Counter(s)
        for i, char in enumerate(s):
            if freqs[char] < k:
                return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i + 1:], k))     
        return len(s)
        