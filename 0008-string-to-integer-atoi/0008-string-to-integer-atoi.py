class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        
        positive = 1
        if i < len(s) and s[i] == "-": positive, i = -1, i + 1
        elif i < len(s) and s[i] == "+": i += 1

        while i < len(s) and s[i] == "0":
            i += 1

        ans = 0
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1
        ans *= positive
        return sorted([-2 ** 31, ans, 2 ** 31 - 1])[1]
        