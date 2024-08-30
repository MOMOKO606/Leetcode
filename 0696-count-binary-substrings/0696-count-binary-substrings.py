class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, prev_count, cur, cur_count, ans = None, 0, s[0], 1, 0
        for j in range(1, len(s)):
            if s[j] == cur: 
                cur_count += 1
            else:
                ans += min(cur_count, prev_count)
                prev, prev_count = cur, cur_count
                cur, cur_count = s[j], 1
        return ans + min(cur_count, prev_count)






        