class Solution:
    def romanToInt(self, s: str) -> int:
        digits = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        if not s: return 0
        if s[:2] in digits: return digits[s[:2]] + self.romanToInt(s[2:])
        else: return digits[s[:1]] + self.romanToInt(s[1:])
        