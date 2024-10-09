class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols, ans = len(matrix), len(matrix[0]), -inf
        for top in range(rows):
            compressed = [0] * cols
            for i in range(top, rows):
                preSum, preSums = 0, [0]
                for j in range(cols):
                    compressed[j] += matrix[i][j]
                    preSum += compressed[j]
                    index = bisect.bisect_left(preSums, preSum - k)
                    if index < len(preSums): ans = max(ans, preSum - preSums[index])
                    bisect.insort(preSums, preSum)
        return ans

                    


        