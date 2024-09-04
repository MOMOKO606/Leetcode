class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            line = []
            for j in range(i):
                line.append(ans[-1][j - 1] + ans[-1][j] if j > 0 else ans[-1][j])
            ans.append(line + [1])
        return ans

            
