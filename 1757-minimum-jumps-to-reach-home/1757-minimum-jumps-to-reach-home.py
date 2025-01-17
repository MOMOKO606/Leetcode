class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        deque, forbidden, boundary = collections.deque([(0, 0, 0)]), set(forbidden), 10000
        while deque:
            pos, prev, steps = deque.popleft()
            if pos == x: return steps
            if pos + a not in forbidden and pos + a <= boundary:
                deque.append([pos + a, a, steps + 1])
                forbidden.add(pos + a)
            if prev > 0 and pos - b >= 0 and pos - b not in forbidden:
                deque.append([pos - b, -b, steps + 1])
        return -1
           

        