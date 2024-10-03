class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = board[0] + board[1]
        moves = {
            0: [1, 3], 
            1: [0, 2, 4], 
            2: [1, 5], 
            3: [0, 4], 
            4: [1, 3, 5], 
            5: [2, 4]
        }
        queue, visited, steps = [board], set([]), 0
        while queue:
            nextQueue = []
            for board in queue:
                if board == [1, 2, 3, 4, 5, 0]: return steps
                k = board.index(0)
                for move in moves[k]:
                    newBoard = board[:]
                    newBoard[k], newBoard[move] = newBoard[move], newBoard[k]
                    if "".join(map(str, newBoard)) not in visited:
                        visited.add("".join(map(str, newBoard)))
                        nextQueue.append(newBoard)
            queue, steps = nextQueue, steps + 1
        return -1


        