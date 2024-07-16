class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(map(len, strs))
        for j in range(m):
            for i in range(len(strs)):
                if i > 0 and strs[i][j] != strs[i - 1][j]:
                    return strs[0][:j]
        return strs[0][:m]


        