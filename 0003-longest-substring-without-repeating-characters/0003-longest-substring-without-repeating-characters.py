class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur, is_valid, i, ans = {}, True, -1, 0
        for j in range(len(s)):
            cur[s[j]] = cur.get(s[j], 0) + 1
            while i < len(s) and cur[s[j]] > 1:
                i += 1
                if i < len(s): 
                    cur[s[i]] -= 1
            ans = max(ans, j - i)
        return ans
        