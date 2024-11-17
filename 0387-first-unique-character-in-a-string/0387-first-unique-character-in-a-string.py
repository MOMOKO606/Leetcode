class Solution:
    def firstUniqChar(self, s: str) -> int:
        target = Counter(s)
        for i, char in enumerate(s):
            if target[char] == 1: return i
        return -1
        