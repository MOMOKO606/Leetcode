class Solution:
    def isNumber(self, s: str) -> bool:
        hasSign, hasDigit, hasDec, hasEe = False, False, False, False
        for char in s:
            if char in "0123456789": hasDigit = True
            elif char in "+-":
                # 不能存在2个+-
                # 不能在digit后再出现+-
                # 不能在小数点后再出现+- 
                if hasSign or hasDigit or hasDec: return False
                hasSign = True
            elif char == ".":
                # 不能存在2个dot
                # Ee后也不能有dot
                if hasDec or hasEe: return False
                hasDec = True
            elif char in "Ee":
                # 不能存在2个Ee
                # Ee前面必须有数字
                # Ee后重制状态
                if hasEe or not hasDigit: return False
                hasEe, hasSign, hasDigit, hasDec = True, False, False, False
            else:
                return False
        return hasDigit
        