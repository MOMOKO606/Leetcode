class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2): s, l = str1, str2
        else: s, l = str2, str1
        ans = ""
        for i in range(1, len(s) + 1):
            divisor = s[:i]
            if divisor * (len(l) // len(divisor)) == l and divisor * (len(s) // len(divisor)) == s:
                ans = max(ans, divisor, key=len)
        return ans
        