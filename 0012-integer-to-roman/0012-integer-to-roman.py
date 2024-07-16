class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        while num:
            if num >= 1000: ans, num = ans + "M", num - 1000
            elif num >= 900: ans, num = ans + "CM", num - 900
            elif num >= 500: ans, num = ans + "D", num - 500
            elif num >= 400: ans, num = ans + "CD", num - 400
            elif num >= 100: ans, num = ans + "C", num - 100
            elif num >= 90: ans, num = ans + "XC", num - 90
            elif num >= 50: ans, num = ans + "L", num - 50
            elif num >= 40: ans, num = ans + "XL", num - 40
            elif num >= 10: ans, num = ans + "X", num - 10
            elif num >= 9: ans, num = ans + "IX", num - 9
            elif num >= 5: ans, num = ans + "V", num - 5
            elif num >= 4: ans, num = ans + "IV", num - 4
            elif num >= 1: ans, num = ans + "I", num - 1
        return ans