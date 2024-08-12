class Solution:
    def isNumber(self, s: str) -> bool:
        hasDigit, hasDec, hasEe, hasSign = False, False, False, False
        for char in s:
            if char in "0123456789":
                hasDigit = True
            elif char in "+-":
                if hasSign or hasDigit or hasDec: return False
                hasSign = True
            elif char == ".":
                if hasEe or hasDec: return False
                hasDec = True
            elif char in "Ee":
                if hasEe or not hasDigit: return False
                hasEe, hasDigit, hasDec, hasSign = True, False, False, False
            else: return False
        return hasDigit
        