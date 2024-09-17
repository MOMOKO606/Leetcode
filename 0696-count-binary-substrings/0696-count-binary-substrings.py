class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur, prev_count, cur_count, ans = None, s[0], 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == cur:
                cur_count += 1
            else:
                ans += min(prev_count, cur_count)
                prev, prev_count, cur, cur_count = cur, cur_count, s[i], 1
        return ans + min(prev_count, cur_count)


        