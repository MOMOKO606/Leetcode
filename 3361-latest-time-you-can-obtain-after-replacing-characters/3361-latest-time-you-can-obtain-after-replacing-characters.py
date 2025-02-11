class Solution:
    def findLatestTime(self, s: str) -> str:
        s = s.split(":")
        digits = [s[0][0], s[0][1], s[1][0], s[1][1]]
        if digits[0] == "?":
            if digits[1] == "?" or int(digits[1]) < 2: digits[0] = "1"
            else: digits[0] = "0"
        if digits[1] == "?":
            if int(digits[0]) == 0: digits[1] = "9"
            else: digits[1] = "1"
        if digits[2] == "?": digits[2] = "5"
        if digits[3] == "?": digits[3] = "9"
        return digits[0] + digits[1] + ":" + digits[2] + digits[3]


        
        
    
        