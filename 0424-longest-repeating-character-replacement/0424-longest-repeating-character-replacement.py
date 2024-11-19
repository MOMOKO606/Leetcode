class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs, maxFreq, ans, i = {}, 0, 0,-1
        for j, char in enumerate(s):
            freqs[char] = freqs.get(char, 0) + 1
            maxFreq = max(maxFreq, freqs[char])
            while j - i > maxFreq + k:
                i += 1
                freqs[s[i]] -= 1
                maxFreq = max(freqs.values())
            ans = max(ans, j - i)
        return ans
            
        