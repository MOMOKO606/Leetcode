class Solution:
    def myAtoi(self, s: str) -> int:
        # Step1. Ignore any leading whitespace
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        # Step2. 
        negative = 1
        if i < len(s) and s[i] == "+":
            i += 1
        elif i < len(s) and s[i] == "-":
            negative = -1
            i += 1

        # Step3
        while i < len(s) and s[i] == "0":
            i += 1

        ans = 0
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1


        return sorted([-2 ** 31, 2 ** 31 - 1, ans * negative])[1]


        

        
        