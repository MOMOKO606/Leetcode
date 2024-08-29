class Solution:
    def isNumber(self, s: str) -> bool:
        hasSign, hasDigit, hasDec, hasEe = False, False, False, False
        for char in s:
            if char in "0123456789":
                hasDigit = True
            elif char in "+-":
                if hasSign or hasDec or hasDigit: return False
                hasSign = True
            elif char == ".":
                if hasEe or hasDec: return False
                hasDec = True
            elif char in "Ee":
                if hasEe or not hasDigit: return False
                hasEe, hasSign, hasDec, hasDigit = True, False, False, False
            else: return False     
        return hasDigit

        