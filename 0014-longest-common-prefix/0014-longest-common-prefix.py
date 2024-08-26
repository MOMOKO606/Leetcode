class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        rows, cols = len(strs), len(shortest)
        for j in range(cols):
            for i in range(rows):
                if i > 0 and strs[i][j] != strs[i - 1][j]: return strs[0][:j]
        return shortest

        