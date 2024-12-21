class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            a_digit = a & 1
            b_digit = b & 1
            c_digit = c & 1
            
            if c_digit:
                if not a_digit and not b_digit: ans += 1
            else:
                ans += a_digit + b_digit
            a >>= 1
            b >>= 1
            c >>= 1
        return ans


        