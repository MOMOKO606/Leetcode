class Solution:
    def isNumber(self, s: str) -> bool:
        hasDigit, hasE, hasDec, hasSign = False, False, False, False
        for char in s:
            if char.isdigit(): hasDigit = True
            elif char in "+-":
                if hasSign or hasDigit or hasDec: return False
                hasSign = True
            elif char == ".":
                if hasDec or hasE: return False
                hasDec = True
            elif char in "eE":
                if not hasDigit or hasE: return False
                hasDigit, hasE, hasDec, hasSign = False, True, False, False
            else: return False
        return hasDigit
        