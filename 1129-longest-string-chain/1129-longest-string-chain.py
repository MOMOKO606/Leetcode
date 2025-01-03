class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @cache
        def dfs_helper(word):
            if word not in word_set: return -inf
            ans = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                ans = max(ans, 1 + dfs_helper(predecessor))
            return ans


        words, ans, word_set = sorted(words, key=len, reverse=True), 1, set(words)
        for word in words:
            ans = max(ans, dfs_helper(word))
        return ans

        