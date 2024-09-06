class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(s):
            if not s: return True
            for word in wordDict:
                k = len(word)
                if s[:k] == word and helper(s[k:]): return True
            return False

        wordDict = set(wordDict)
        return helper(s)
        