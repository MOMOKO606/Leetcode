class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count, n = count + 1, n & (n - 1)
        return count


        