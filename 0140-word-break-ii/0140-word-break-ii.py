class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(s, seq):
            if not s: 
                self.ans.append(" ".join(seq))
                return True
            for word in wordDict:
                k = len(word)
                if s[:k] == word:
                    helper(s[k:], seq + [word])

        self.ans = []
        helper(s, [])
        return self.ans
        
        