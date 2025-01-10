class FenwickTree:
    def __init__(self, value, size):
        self.nums = [value] * size
        self.size = size

    def _lowbit(self, index):
        return index & -index

    def update(self, index, delta):
        while index < self.size:
            self.nums[index] += delta
            index += self._lowbit(index)
    
    def query(self, index):
        ans = 0
        while index:
            ans += self.nums[index]
            index -= self._lowbit(index)
        return ans

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        transfer = {num: i + 1 for i, num in enumerate(sorted(set(instructions)))}
        ft, ans = FenwickTree(value=0, size=len(transfer) + 1), 0
        for i, num in enumerate(instructions):
            k = transfer[num]
            ft.update(k, 1)
            ans += min(ft.query(k - 1), i + 1 - ft.query(k))
        return ans % (10 ** 9 + 7)

        