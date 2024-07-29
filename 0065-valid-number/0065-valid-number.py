class Solution:
    def isNumber(self, s: str) -> bool:
        # Ee只能出现1次，且不能在最前和最后
        # Ee之前可以写一个带符号的整数 / 实数
        # Ee之后也可以写一个带符号的整数
        # 所以Ee可以看作一个分隔符，当碰到valid的Ee之后，状态重制
        hasDigit, hasDec, hasE, hasSymbol = False, False, False, False
        for char in s:
            if char in "0123456789": hasDigit = True
            # 正负号前只能为空 或 Ee
            # 即正负号前面有正负号/./数字都不行
            elif char in "+-": 
                if hasSymbol or hasDigit or hasDec: return False
                else: hasSymbol = True
            # Ee只能出现1次，且前面必须存在数字
            elif char in "Ee":
                if not hasDigit or hasE: return False
                else: hasE, hasSymbol, hasDigit, hasDec = True, False, False, False
            elif char == ".":
                if hasDec or hasE: return False
                else: hasDec = True
            else: return False
        return hasDigit
        