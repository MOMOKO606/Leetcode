class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur, is_valid, i, j, ans = {}, True, -1, -1, 0
        while i <= j:
            if j < len(s) and is_valid:
                j += 1
                if j < len(s):
                    cur[s[j]] = cur.get(s[j], 0) + 1
                    if cur[s[j]] > 1: is_valid = False
                    else: ans = max(ans, j - i)
            else:
                i += 1
                if i < len(s):
                    cur[s[i]] -= 1
                    if cur[s[i]] == 1:
                        is_valid = True 
        return ans
        