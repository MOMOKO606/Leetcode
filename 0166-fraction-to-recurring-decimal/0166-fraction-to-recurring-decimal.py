class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator % denominator: return str(numerator // denominator)
        negative = "" if numerator * denominator >= 0 else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        ans, seen = negative + str(numerator // denominator) + ".", {}
        numerator %= denominator
        while numerator:
            numerator *= 10
            if numerator in seen: 
                i = seen[numerator] 
                return ans[:i] + "(" + ans[i:] + ")"
            seen[numerator] = len(ans)
            ans += str(numerator // denominator)
            numerator %= denominator
        return ans

        