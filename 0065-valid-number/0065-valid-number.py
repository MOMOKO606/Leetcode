class Solution:
    def isNumber(self, s: str) -> bool:
        hasDec, hasSign, hasDigit, hasEe = False, False, False, False
        for char in s:
            if char in "0123456789":
                hasDigit = True
            elif char == ".":
                if hasDec or hasEe: return False
                hasDec = True
            elif char in "+-":
                if hasSign or hasDec or hasDigit: return False
                hasSign = True
            elif char in "Ee":
                if hasEe or not hasDigit: return False
                hasEe, hasSign, hasDigit, hasDec = True, False, False, False
            else: return False
        return hasDigit
        