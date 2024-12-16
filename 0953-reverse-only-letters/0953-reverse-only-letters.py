class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j, s = 0, len(s) - 1, list(s)
        while i < j:
            if not s[i].isalpha(): i += 1
            elif not s[j].isalpha(): j -= 1
            else: s[i], s[j], i, j = s[j], s[i], i + 1, j - 1 
        return "".join(s)


        