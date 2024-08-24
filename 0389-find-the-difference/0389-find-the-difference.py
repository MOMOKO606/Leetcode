class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        target = Counter(s)
        for char in t:
            if char not in target or target[char] == 0: return char
            target[char] -= 1
        