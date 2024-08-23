class Solution:
    def intToRoman(self, num: int) -> str:
        if not num: return ""
        if num >= 1000:
            return "M" + self.intToRoman(num - 1000)
        elif 1000 > num >= 900:
            return "CM" + self.intToRoman(num - 900)
        elif 900 > num >= 500:
            return "D" + self.intToRoman(num - 500)
        elif 500 > num >= 400:
            return "CD" + self.intToRoman(num - 400)
        elif 400 > num >= 100:
            return "C" + self.intToRoman(num - 100)
        elif 100 > num >= 90:
            return "XC" + self.intToRoman(num - 90)
        elif 90 > num >= 50:
            return "L" + self.intToRoman(num - 50)
        elif 50 > num >= 40:
            return "XL" + self.intToRoman(num - 40)
        elif 40 > num >= 10:
            return "X" + self.intToRoman(num - 10)
        elif 10 > num >= 9:
            return "IX" + self.intToRoman(num - 9)
        elif 9 > num >= 5:
            return "V" + self.intToRoman(num - 5)
        elif 5 > num >= 4:
            return "IV" + self.intToRoman(num - 4)
        elif 4 > num >= 1:
            return "I" + self.intToRoman(num - 1)
        