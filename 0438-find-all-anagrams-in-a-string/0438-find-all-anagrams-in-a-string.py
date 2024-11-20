class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freqs, n, i, ans = Counter(p), len(p), 0, []
        for j in range(len(s) + 1):
            if not n: ans.append(i)
            if i < len(s) and j - i + 1 > len(p):
                if s[i] in freqs:
                    freqs[s[i]] += 1
                    if freqs[s[i]] > 0: n += 1
                i += 1
            
            if j < len(s) and s[j] in freqs:
                freqs[s[j]] -= 1
                if freqs[s[j]] >= 0: n -= 1
        return ans