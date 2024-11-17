class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        target = Counter(s)
        for i, char in enumerate(t):
            if not target.get(char, 0): return char
            target[char] -= 1
        