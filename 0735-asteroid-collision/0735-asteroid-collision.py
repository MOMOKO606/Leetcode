class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            next = asteroid
            while stack and stack[-1] > 0 and next < 0:
                cur = stack.pop()
                if abs(cur) == abs(next): break
                elif abs(cur) > abs(asteroid): next = cur
            else: stack.append(next)
        return stack
        