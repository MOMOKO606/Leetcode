class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        target = Counter(s)
        for i, char in enumerate(s):
            if target[char] < k: break
        else:
            return len(s)
        return max( self.longestSubstring(s[:i], k), self.longestSubstring(s[i + 1:], k))
        