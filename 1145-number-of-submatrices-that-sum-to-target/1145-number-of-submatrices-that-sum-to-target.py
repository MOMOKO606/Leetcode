class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols, ans = len(matrix), len(matrix[0]), 0
        for top in range(rows):
            compressed = [0] * cols
            for bottom in range(top, rows):
                preSums, preSum = {0: 1}, 0
                for j in range(cols):
                    compressed[j] += matrix[bottom][j]
                    preSum += compressed[j]
                    ans += preSums.get(preSum - target, 0)
                    preSums[preSum] = preSums.get(preSum, 0) + 1
        return ans



