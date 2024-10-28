class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n or k == 0: return [[]]
        ans = []
        for num in range(n, 0, -1):
            if num >= k:
                ans += [[num] + seq for seq in self.combine(num - 1, k - 1)]
        return ans


        