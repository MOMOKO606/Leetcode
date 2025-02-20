class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        dp = {word: 1 for word in words}
        for word in words:
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
        return max(dp.values())


        