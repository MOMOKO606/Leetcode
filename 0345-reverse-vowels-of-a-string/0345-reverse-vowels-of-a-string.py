class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j, vowels, s = 0, len(s) - 1, "aeiou", list(s)
        while i < j:
            if i < len(s) and not s[i].lower() in vowels: 
                i += 1
            elif not s[j].lower() in vowels: 
                j -= 1
            else: 
                s[i], s[j], i, j = s[j], s[i], i + 1, j - 1
        return "".join(s)
        