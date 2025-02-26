class FenwickTree:
    def __init__(self, size, value):
        self.size = size
        self.nums = [value] * size

    def lowbit(self, index):
        return index & -index

    def update(self, index, delta):
        while index < self.size:
            self.nums[index] += delta
            index += self.lowbit(index)

    def query(self, index):
        ans = 0
        while index:
            ans += self.nums[index]
            index -= self.lowbit(index)
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        trans = {num: i + 1 for i, num in enumerate(sorted(instructions))}
        ft, ans = FenwickTree(len(instructions) + 1, 0), 0
        for i, instruction in enumerate(instructions):
            k = trans[instruction]
            ft.update(k, 1)
            ans += min(ft.query(k - 1), i - ft.query(k) + 1)
        return ans % (10 ** 9 + 7)

        