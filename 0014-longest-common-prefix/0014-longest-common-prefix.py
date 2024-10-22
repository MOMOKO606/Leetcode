class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rows, cols = len(strs), len(min(strs, key=len))
        for j in range(cols):
            for i in range(rows):
                if i > 0 and strs[i][j] != strs[i - 1][j]: 
                    return strs[i][:j]
        return strs[0][:cols]
        