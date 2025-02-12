class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans, i, left_end, right_end, mid = "", 0, 97, 122, 110
        while k and i < len(s):
            if ord(s[i]) > mid and k >= right_end - ord(s[i]) + 1:
                delta, ans = right_end - ord(s[i]) + 1, ans + "a"
            else:
                delta = min(k, ord(s[i]) - left_end)
                ans += chr(ord(s[i]) - delta)
            i += 1
            k -= delta         
        return ans + s[i:]
        