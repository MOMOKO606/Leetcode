class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2): l, s = str1, str2
        else: l, s = str2, str1
        ans = ""
        for i in range(1, len(s) + 1):
            divisor = s[:i]
            k = len(divisor)
            if not len(s) % k and not len(l) % k: 
                if divisor * (len(s) // k) == s and divisor * (len(l) // k) == l:
                    ans = divisor
        return ans
        