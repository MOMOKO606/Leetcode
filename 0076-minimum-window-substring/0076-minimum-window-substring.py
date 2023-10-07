class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, count, i, j, smallest, left, right = collections.Counter(t), len(t), -1, -1, math.inf, -1, -1
        while i <= j:
            if not count and j - i < smallest: smallest, left, right = j - i, i + 1, j
            if count > 0 and j < len(s):
                j += 1
                if j < len(s) and s[j] in target:
                    target[s[j]] -= 1
                    if target[s[j]] >= 0: count -= 1
            else:
                i += 1
                if i < len(s) and s[i] in target:
                    target[s[i]] += 1
                    if target[s[i]] > 0: count += 1   
        return s[left: right + 1]