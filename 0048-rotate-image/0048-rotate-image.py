class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def next_position(i, j, di, dj, steps):
            while steps:
                if not (left <= i + di <= right and top <= j + dj <= bottom):
                    di, dj = dj, -di
                steps, i, j = steps - 1, i + di, j + dj
            return i, j, di, dj

        def move_4_points(i, j, steps):
            to_be_moved, di, dj = matrix[i][j], 0, 1
            for _ in range(4):
                next_i, next_j, di, dj = next_position(i, j, di, dj, steps)
                matrix[next_i][next_j], to_be_moved, i, j = to_be_moved, matrix[next_i][next_j], next_i, next_j

        left, right, top, bottom = 0, len(matrix) - 1, 0, len(matrix) - 1
        while left < right:
            for j in range(left, right):
                move_4_points(top, j, right - left)
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

                 
