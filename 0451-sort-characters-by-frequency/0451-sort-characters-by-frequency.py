class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        for char, freq in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True):
            ans += char * freq
        return ans        