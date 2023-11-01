class Solution:
    def intToRoman(self, num: int) -> str:
        def helper(num):
            if not num: return ""
            if num >= 1000: return trans[1000] + helper(num - 1000)
            elif num >= 900: return trans[900] + helper(num - 900)
            elif num >= 500: return trans[500] + helper(num - 500)
            elif num >= 400: return trans[400] + helper(num - 400)
            elif num >= 100: return trans[100] + helper(num - 100)
            elif num >= 90: return trans[90] + helper(num - 90)
            elif num >= 50: return trans[50] + helper(num - 50)
            elif num >= 40: return trans[40] + helper(num - 40)
            elif num >= 10: return trans[10] + helper(num - 10)
            elif num >= 9: return trans[9] + helper(num - 9)
            elif num >= 5: return trans[5] + helper(num - 5)
            elif num >= 4: return trans[4] + helper(num - 4)
            else: return trans[1] + helper(num - 1)
        trans = {1: "I", 4: "IV", 5: "V", 
                         9: "IX", 10: "X", 
                         40: "XL", 50: "L", 
                         90: "XC", 100: "C",
                         400: "CD", 500: "D",
                         900: "CM", 1000: "M"}
        return helper(num)