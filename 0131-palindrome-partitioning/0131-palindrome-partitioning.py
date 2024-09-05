class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(s, seq):
            if not s: 
                self.ans.append(seq[:])
                return 
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], seq + [s[:i]])

        self.ans = []
        helper(s, [])
        return self.ans

        