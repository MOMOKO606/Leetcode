class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words, chains, ans = sorted(words, key=len), {word: 1 for word in words}, 1
        for word in words:
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                chains[word] = max(chains[word], chains.get(predecessor, 0) + 1)
            ans = max(ans, chains[word])
        return ans