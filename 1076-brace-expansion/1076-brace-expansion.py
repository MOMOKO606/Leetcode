class Solution:
    def expand(self, s: str) -> List[str]:
        def getOptions(s):
            options = []
            for j, char in enumerate(s):
                if char.isalpha(): options.append(char)
                if char == "}": break
            return options, j + 1


        def helper(s, seq):
            if not s: 
                ans.append(seq[:])
                return
            if s[0].isalpha(): 
                helper(s[1:], seq + s[0])
            else:
                options, j = getOptions(s)
                for char in options:
                    helper(s[j:], seq + char)

        ans = []
        helper(s, "")
        return sorted(ans)
        