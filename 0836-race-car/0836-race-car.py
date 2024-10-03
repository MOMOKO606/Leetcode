class Solution:
    def racecar(self, target: int) -> int:
        deque = collections.deque([(0, 1, 0)])
        while deque:
            pos, speed, steps = deque.popleft()
            if pos == target: return steps
            deque.append((pos + speed, speed * 2, steps + 1))
            if (speed > 0 and pos + speed > target) or (speed < 0 and pos + speed < target):
                deque.append((pos, -speed / abs(speed), steps + 1))

        

        


        