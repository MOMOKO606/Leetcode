class Solution:
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2: return 0
        if not word1: return len(word2)
        if not word2: return len(word1)
        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        else:
            return 1 + min(self.minDistance(word1[:-1], word2[:-1]), self.minDistance(word1[:-1], word2), self.minDistance(word1, word2[:-1]))
        