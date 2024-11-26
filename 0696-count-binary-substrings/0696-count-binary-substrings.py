class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur, ans, prev = 1, 0, None
        for j in range(1, len(s)):
            if s[j] == s[j - cur]: 
                cur += 1
                if prev and cur <= prev: ans += 1
            else:
                prev, cur, ans = cur, 1, ans + 1
        return ans
                
        