class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(s=s):
            if not s: return True
            for word in wordSet:
                k = len(word)
                if s[:k] == word:
                    if helper(s[k:]): return True
            return False
        
        wordSet = set(wordDict)
        return helper()
        
        

        