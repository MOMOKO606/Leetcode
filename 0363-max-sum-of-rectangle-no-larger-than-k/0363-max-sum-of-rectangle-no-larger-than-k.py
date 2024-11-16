class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols, ans = len(matrix), len(matrix[0]), -inf
        for top in range(rows):
            compressed = [0] * cols
            for bottom in range(top, rows):
                preSum, preSums = 0, [0]
                for j in range(cols):
                    compressed[j] += matrix[bottom][j]
                    preSum += compressed[j]
                    i = bisect.bisect_left(preSums, preSum - k)
                    if i < len(preSums): ans = max(ans, preSum - preSums[i])
                    bisect.insort(preSums, preSum)
        return ans

                