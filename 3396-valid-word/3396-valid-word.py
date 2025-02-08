class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        hasVow, hasCons, word = False, False, word.lower()
        for char in word:
            if char.isalpha():
                if char in "aeiou": hasVow = True
                else: hasCons = True
            elif not char.isdigit(): return False
        return hasVow and hasCons
            

        