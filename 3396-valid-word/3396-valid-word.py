class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        hasVowel, hasCons = False, False
        for char in word:
            if not char.isalnum(): return False
            if char.lower() in "aeiou": hasVowel = True
            elif char.isalpha(): hasCons = True
        return hasVowel and hasCons

        