class Solution:
    def isNumber(self, s: str) -> bool:
        hasDigit, hasEe, hasSign, hasDec = False, False, False, False
        for char in s:
            if char in "0123456789":
                hasDigit = True
            elif char in "+-":
                if hasSign or hasDec or hasDigit: return False
                hasSign = True
            elif char == ".":
                if hasDec or hasEe: return False
                hasDec = True
            elif char in "Ee":
                if hasEe or not hasDigit: return False
                hasDigit, hasEe, hasSign, hasDec = False, True, False, False
            else:
                return False
        return hasDigit
        