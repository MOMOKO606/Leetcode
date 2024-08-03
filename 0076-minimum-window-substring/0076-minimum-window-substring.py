class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, i, j, remain, ans, l, r = Counter(t), -1, -1, len(t), inf, -1, -1
        while i <= j:
            if not remain: 
                if j - i < ans: ans, l, r = j - i, i, j
            if j < len(s) and remain > 0:
                j += 1
                if j < len(s) and s[j] in target:
                    target[s[j]] -= 1
                    if target[s[j]] >= 0: remain -= 1
            else:
                i += 1
                if i < len(s) and s[i] in target:
                    target[s[i]] += 1
                    if target[s[i]] > 0: remain += 1
        return s[l + 1: r + 1]
                

        