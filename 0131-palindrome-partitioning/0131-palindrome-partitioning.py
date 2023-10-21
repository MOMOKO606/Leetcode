class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalind(s):
            i, j = 0, len(s) - 1
            while i <= j and s[i] == s[j]:
                i, j = i + 1, j - 1
            return i >= j

        if not s: return [[]]
        ans = []
        for i in range(len(s)):
            if not isPalind(s[:i + 1]): continue
            ans += [[s[:i + 1]] + seq for seq in self.partition(s[i + 1:])]
        return ans

        