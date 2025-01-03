class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words, visited, ans = sorted(words, key=len), {word: 1 for word in words}, 1
        for word in words:
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in visited:
                    visited[word] = max(visited[word], visited[predecessor] + 1)
            ans = max(ans, visited[word])
        return ans

        