class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k: return [[]]    
        return [[num] + seq for num in range(n, k - 1, -1) for seq in self.combine(num - 1, k - 1)]

        