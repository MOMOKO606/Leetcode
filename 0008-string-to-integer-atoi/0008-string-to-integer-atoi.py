class Solution:
    def myAtoi(self, s: str) -> int:
        # Step1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        # Step2
        negative = 1
        if i < len(s):
            if s[i] == "+": 
                negative, i = 1, i + 1
            elif s[i] == "-": 
                negative, i = -1, i + 1

        # Step 3
        while i < len(s) and s[i] == "0":
            i += 1
        
        ans = 0
        while i < len(s) and s[i].isdecimal():
            ans = ans * 10 + int(s[i])
            i += 1

        # Step 4
        ans = ans * negative
        return sorted([-2 ** 31, ans, 2 ** 31 - 1])[1]
            

            

        