class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        target = Counter(s)
        for i, char in enumerate(s):
            if target[char] < k:
                left, right = self.longestSubstring(s[:i], k), self.longestSubstring(s[i + 1:], k)
                return max(left, right)
        return len(s) 
        