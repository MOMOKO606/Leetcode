class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not (numerator % denominator): return str(numerator // denominator)
        ans = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        ans, pos = ans + str(numerator // denominator) + ".", {}
        numerator %= denominator
        while numerator:
            numerator *= 10
            if numerator in pos: 
                i = pos[numerator]
                return ans[:i] + "(" + ans[i:] + ")"
            pos[numerator] = len(ans)
            ans += str(numerator // denominator)
            numerator %= denominator
        return ans
        