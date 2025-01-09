class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1, word2, ans = list(word1), list(word2), []
        while word1 and word2:
            ans += word1.pop(0)
            ans += word2.pop(0)
        ans += word1 or word2
        return "".join(ans)
        