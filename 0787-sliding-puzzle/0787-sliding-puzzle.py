class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        board = board[0] + board[1]
        queue, visited, steps = [board], set([]), 0
        while queue:
            next_queue = []
            for board in queue:
                if board == [1, 2, 3, 4, 5, 0]: return steps
                i = board.index(0)
                for j in moves[i]:
                    new_board = board[:]
                    new_board[i], new_board[j] = new_board[j], new_board[i]
                    record = "".join(map(str, new_board))
                    if record in visited: continue
                    visited.add(record)
                    next_queue.append(new_board)
            queue, steps = next_queue, steps + 1
        return -1
        