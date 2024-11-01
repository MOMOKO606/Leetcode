class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def helper(s, n, seq):
            if not n and not s: 
                ans.append(seq)
                return
            if not n or not s: return
            if 0 <= int(s[0]) < 10: helper(s[1:], n - 1, seq + [str(s[0])])
            if 9 < int(s[:2]) < 100: helper(s[2:], n - 1, seq + [str(s[:2])])
            if 100 <= int(s[:3]) < 256: helper(s[3:], n - 1, seq + [str(s[:3])])


        ans = []
        helper(s, 4, [])
        return [".".join(seq) for seq in ans]

        