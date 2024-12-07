class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def helper(i, seq):
            if i == len(s): 
                ans.append(seq[:])
                return
            for j in range(i + 1, len(s) + 1):
                if s[i: j] == s[i: j][::-1]:
                    helper(j, seq + [s[i: j]])


        ans = []
        helper(i=0, seq=[])
        return ans

        