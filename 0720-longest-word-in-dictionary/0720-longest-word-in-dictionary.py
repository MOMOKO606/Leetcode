class Solution:
    def longestWord(self, words: List[str]) -> str:
        words, visited, ans = sorted(words), set([""]), ""
        for word in words:
            if word[:-1] in visited:
                visited.add(word)
                ans = max(ans, word, key=len)
        return ans


        