class FenwickTree:
    def __init__(self, size, value):
        self.size = size
        self.tree = [value] * size

    def _lowbit(self, index):
        return index & -index

    def update(self, index, delta):
        while index < self.size:
            self.tree[index] += delta
            index += self._lowbit(index)

    def query(self, index):
        ans = 0
        while index:
            ans += self.tree[index]
            index -= self._lowbit(index)
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        transfer = {num: i + 1 for i, num in enumerate(sorted(set(instructions)))}
        fw = FenwickTree(len(transfer) + 1, 0)
        ans = 0
        for i, num in enumerate(instructions):
            index = transfer[num]
            left = fw.query(index - 1)
            fw.update(index, 1)
            right = i - fw.query(index) + 1
            ans += min(left, right)
        return ans % (10 ** 9 + 7)

        