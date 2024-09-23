class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i, ans, freqs = -1, 1, collections.defaultdict(int)
        for j in range(len(s)):
            freqs[s[j]] += 1
            while len(freqs) > 2:
                i += 1
                freqs[s[i]] -= 1
                if not freqs[s[i]]: del freqs[s[i]]
            ans = max(ans, j - i)
        return ans

        