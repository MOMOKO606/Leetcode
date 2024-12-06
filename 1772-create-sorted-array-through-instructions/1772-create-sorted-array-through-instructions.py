class FenwickTree:
    def __init__(self, size, value):
        self.ft = [value] * size
        self.size = size

    def __lowbit(self, index):
        return index & -index

    def update(self, index, delta):
        while index < self.size:
            self.ft[index] += delta
            index += self.__lowbit(index)

    def query(self, index):
        ans = 0
        while index:
            ans += self.ft[index]
            index -= self.__lowbit(index)
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        transfer, ans = {num: i + 1 for i, num in enumerate(sorted(set(instructions)))}, 0
        ft = FenwickTree(len(transfer) + 1, 0)
        for j, num in enumerate(instructions):
            i = transfer[num]
            ft.update(i, 1)
            ans += min(ft.query(i - 1), j - ft.query(i) + 1)
        return ans % (10 ** 9 + 7)


        