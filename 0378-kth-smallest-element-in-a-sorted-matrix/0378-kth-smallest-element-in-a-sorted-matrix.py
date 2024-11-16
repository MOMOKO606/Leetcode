class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def helper(mid):
            count = 0
            for i in range(rows):
                count += bisect.bisect_right(matrix[i], mid)
            return count


        low, high, rows, cols = matrix[0][0], matrix[-1][-1], len(matrix), len(matrix[0])
        if k == 1: return low
        if k == rows * cols: return high
        while low <= high:
            mid = (low + high) // 2
            pivot = helper(mid)
            if pivot >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low

        