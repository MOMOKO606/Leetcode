class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target = Counter(magazine)
        for char in ransomNote:
            if char not in target or not target[char]: return False
            target[char] -= 1
        return True
        