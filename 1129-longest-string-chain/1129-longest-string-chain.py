class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words, visited, ans = sorted(words, key = lambda x: len(x)), {}, -math.inf
        for word in words:
            curLength = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                curLength = max(curLength, visited.get(prev, 0) + 1)
            visited[word] = curLength
            ans = max(ans, curLength)
        return ans


        