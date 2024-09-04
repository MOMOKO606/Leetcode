class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_line = []
        for i in range(rowIndex + 1):
            ans = []
            for j in range(i):
                ans.append(prev[j - 1] + prev[j] if j > 0 else prev[j])
            ans += [1]
            prev = ans
        return ans


        