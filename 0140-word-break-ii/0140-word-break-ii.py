class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def helper(s=s, seq=[]):
            if not s:
                ans.append(" ".join(seq))
                return
            for word in wordDict:
                if s[:len(word)] == word:
                    helper(s[len(word):], seq + [word])

        wordSet, ans = set(wordDict), []
        helper()
        return ans

        