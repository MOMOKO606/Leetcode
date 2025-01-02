class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        chains, ans, words = {word: 1 for word in words}, 1, sorted(words, key=len)
        for word in words:
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in chains:
                    chains[word] = max(chains[word], chains[predecessor] + 1)
            ans = max(ans, chains[word])
        return ans



        