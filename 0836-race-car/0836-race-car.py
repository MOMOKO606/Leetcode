class Solution:
    def racecar(self, target: int) -> int:
        queue, steps = [(0, 1)], 0
        while queue:
            next_queue = []
            for pos, speed in queue:
                if pos == target: return steps
                next_queue.append((pos + speed, speed * 2))
                if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                    next_queue.append((pos, -speed / abs(speed))) 
            queue, steps = next_queue, steps + 1
        

        