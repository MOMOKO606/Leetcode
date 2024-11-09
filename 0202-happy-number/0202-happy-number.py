class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited: return False
            visited.add(n)
            next_n = 0
            while n:
                digit = n % 10
                next_n += digit * digit
                n //= 10
            n = next_n
        return True
        