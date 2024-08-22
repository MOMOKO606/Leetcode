class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        i, j, remain, ans = -1, -1, k, "$" * (len(s) + 1)
        while i <= j:
            if remain == 0:
                ans = min(ans, s[i + 1: j + 1], key=lambda x:(len(x), x))
            if j < len(s) and remain > 0:
                j += 1
                if j < len(s) and s[j] == "1":
                    remain -= 1
            else:
                i += 1
                if i < len(s) and s[i] == "1":
                    remain += 1
        return ans if "$" not in ans else ""


        