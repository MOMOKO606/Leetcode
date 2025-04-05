class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rows, cols, ans = len(strs), len(min(strs, key=len)), ""
        for j in range(cols):
            for i in range(1, rows):
                if strs[i][j] != strs[i - 1][j]:
                    return strs[i][:j]
        return strs[0][:cols]


        