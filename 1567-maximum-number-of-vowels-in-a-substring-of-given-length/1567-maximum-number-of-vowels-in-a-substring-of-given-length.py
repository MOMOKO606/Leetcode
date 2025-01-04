class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans, i, count = 0, -1, 0
        for j, char in enumerate(s):
            if char in "aeiou": count += 1
            if j - i > k: 
                i += 1
                if s[i] in "aeiou": count -= 1
            ans = max(ans, count)
        return ans

        