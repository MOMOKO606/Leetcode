class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @cache
        def dfsHelper(node):
            if node not in word_set: return 0
            ans = 0
            for i in range(len(node)):
                predecessor = node[:i] + node[i + 1:]
                ans = max(ans, dfsHelper(predecessor) + 1)
            return ans

        word_set = set(words)
        ans = 1
        for word in words:
            ans = max(ans, dfsHelper(word))
        return ans
        