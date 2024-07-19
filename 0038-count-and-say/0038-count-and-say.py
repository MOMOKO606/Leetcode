class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s):
            ans, count = "", 1
            for i in range(1, len(s)):
                if s[i] != s[i - 1]:
                    ans, count = ans + str(count) + s[i - 1], 1
                elif s[i] == s[i - 1]:
                    count += 1
            return ans + str(count) + s[-1]

        if n == 1: return str(n)
        return rle(self.countAndSay(n - 1))



        