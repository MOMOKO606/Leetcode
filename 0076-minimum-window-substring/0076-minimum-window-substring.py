class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j, count, remain, ans, l, r = -1, -1, Counter(t), len(t), inf, 0, 0
        while i <= j:
            if not remain: 
                if j - i < ans:
                    ans, l, r = j - i, i, j
            if j < len(s) and remain:
                j += 1
                if j < len(s) and s[j] in count:
                    count[s[j]] -= 1
                    if count[s[j]] >= 0: remain -= 1
            else:
                i += 1
                if i < len(s) and s[i] in count:
                    count[s[i]] += 1
                    if count[s[i]] > 0: remain += 1
        return s[l + 1: r + 1]
        