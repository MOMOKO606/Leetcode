class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def move_all(i, j, steps):
            N, to_be_moved, di, dj = 4, matrix[i][j], 0, 1
            while N:
                next_i, next_j, di, dj = get_next(i, j, di, dj, steps)
                matrix[next_i][next_j], to_be_moved = to_be_moved, matrix[next_i][next_j]
                i, j = next_i, next_j
                N -= 1

        def get_next(i, j, di, dj, steps):
            while steps:
                if not (top <= i + di <= bottom and left <= j + dj <= right):
                    di, dj = dj, -di
                i, j, steps = i + di, j + dj, steps - 1
            return i, j, di, dj


        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix) - 1
        while top < bottom:
            steps = n = right - left
            i, j = top, left
            while n:
                move_all(i, j, steps)
                j += 1
                n -= 1
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1