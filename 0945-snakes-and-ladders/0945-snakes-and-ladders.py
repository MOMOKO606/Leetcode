class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        i, j, dj, cur, pos = n - 1, 0, 1, 1, {}
        while cur <= n * n:
            pos[cur], cur = (i, j), cur + 1
            if not (0 <= j + dj < n): i, dj = i - 1, -dj
            else: j += dj
        
        queue, ans, visited = [1], 0, set([cur])
        while queue:
            next_queue = []
            for node in queue:
                if node == n * n: return ans
                for move_to in range(node + 1, min(node + 6, n * n) + 1):
                    if move_to in visited: continue
                    visited.add(move_to)
                    i, j = pos[move_to]
                    if board[i][j] == -1:
                        next_queue.append(move_to)
                    else:
                        next_queue.append(board[i][j])
            queue, ans = next_queue, ans + 1
        return -1

                   

        