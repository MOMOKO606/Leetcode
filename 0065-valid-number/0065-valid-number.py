class Solution:
    def isNumber(self, s: str) -> bool:
        hasDigit, hasDec, hasE, hasSymbol = False, False, False, False
        for char in s:
            if char in "0123456789": hasDigit = True
            elif char in "+-":
                if hasSymbol or hasDigit or hasDec: return False
                else: hasSymbol = True
            elif char in "Ee":
                if not hasDigit or hasE: return False
                else: hasE, hasSymbol, hasDigit, hasDec = True, False, False, False
            elif char == ".":
                if hasDec or hasE: return False
                else: hasDec = True
            else: return False
        return hasDigit
        