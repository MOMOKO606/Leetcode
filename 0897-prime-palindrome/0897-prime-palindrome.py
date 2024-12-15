class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            for divisor in range(2, int(num ** 0.5) + 1):
                if not num % divisor: return False
            return True

        if n < 3: return 2
        if 7 < n <= 11: return 11
        i = 2
        while True:
            num = int(str(i) + str(i)[::-1][1:])
            if num >= n and is_prime(num):
                return num
            i += 1
        