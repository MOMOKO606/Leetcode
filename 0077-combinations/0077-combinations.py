class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k: return [[]]
        return [[i] + seq for i in range(n, k - 1, -1) for seq in self.combine(i - 1, k - 1)]
        