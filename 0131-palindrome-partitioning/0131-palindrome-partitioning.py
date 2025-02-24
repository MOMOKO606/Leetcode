class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(s=s, seq=[]):
            if not s: 
                ans.append(seq)
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], seq + [s[:i]])

        ans = []
        helper()
        return ans
        