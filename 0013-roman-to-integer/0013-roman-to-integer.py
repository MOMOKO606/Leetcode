class Solution:
    def romanToInt(self, s: str) -> int:
        two_digits = {
            "IV": 4, "IX": 9, "XL": 40, "XC": 90,
            "CD": 400, "CM": 900
        }
        one_digit = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        
        def helper(s):
            if not s: return 0
            if s[:2] in two_digits:
                return two_digits[s[:2]] + helper(s[2:])
            return one_digit[s[0]] + helper(s[1:]) 

        return helper(s)
        