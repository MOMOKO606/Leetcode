class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            line = [ans[i - 1][j - 1] + ans[i - 1][j] for j in range(1, len(ans[i - 1]))]
            ans.append([1] + line + [1])
        return ans


        