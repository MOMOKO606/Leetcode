class Solution:
    def romanToInt(self, s: str) -> int:
        if not s: return 0
        transfer = {
            "I": 1, "IV": 4, "V": 5, "IX": 9,
            "X": 10, "XL": 40, "L": 50, "XC": 90, 
            "C": 100, "CD": 400, "D": 500, "CM": 900,
            "M": 1000
            }
        if len(s) > 1 and s[:2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            return transfer[s[:2]] + self.romanToInt(s[2:])
        return transfer[s[:1]] + self.romanToInt(s[1:])

        