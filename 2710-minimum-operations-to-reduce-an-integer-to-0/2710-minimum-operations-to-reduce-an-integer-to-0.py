class Solution:
    @cache
    def minOperations(self, n: int) -> int:
        root = log2(n) 
        if root == int(root): return 1
        left, right = 2 ** floor(root), 2 ** ceil(root)
        return 1 + min(self.minOperations(n - left), self.minOperations(right - n))
        