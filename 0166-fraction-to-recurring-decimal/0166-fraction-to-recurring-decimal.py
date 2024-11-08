class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator % denominator: return str(numerator // denominator)
        ans = "" if numerator * denominator > 0 else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        ans, visited = ans + str(numerator // denominator) + ".", {}
        numerator %= denominator
        while numerator:
            numerator *= 10
            if numerator in visited: 
                i = visited[numerator]
                return ans[:i] + "(" + ans[i:] + ")"
            visited[numerator] = len(ans)
            ans += (str(numerator // denominator))
            numerator %= denominator
        return ans
        

        