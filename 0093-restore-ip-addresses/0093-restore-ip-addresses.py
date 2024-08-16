class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def helper(i=0, j=0, seq=""):
            if i == len(s) and j == 4: 
                ans.append(seq[:-1])
                return
            if i == len(s) or j == 4: return 
            helper(i + 1, j + 1, seq + s[i] + ".")
            if 10 <= int(s[i: i + 2]) <= 99: helper(i + 2, j + 1, seq + s[i: i + 2] + ".")
            if 100 <= int(s[i: i + 3]) <= 255: helper(i + 3, j + 1, seq + s[i: i + 3] + ".")

        ans = []
        helper()
        return ans
        