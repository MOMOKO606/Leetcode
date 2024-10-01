class FenwickTree:
    def __init__(self, size, value):
        self.tree = [value] * size
        self.size = size

    def __lowbit(self, index):
        return index & -index

    def update(self, index, delta):
        while index < self.size:
            self.tree[index] += delta
            index += self.__lowbit(index)
    
    def query(self, index):
        ans = 0
        while index:
            ans += self.tree[index]
            index -= self.__lowbit(index)
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        transfer = {num: i + 1 for i, num in enumerate(sorted(set(instructions)))}
        ft, ans = FenwickTree(len(transfer) + 1, 0), 0
        for i, num in enumerate(instructions):
            k = transfer[num]
            ans += min(ft.query(k - 1), i - ft.query(k))
            ft.update(k, 1)
        return ans % (10 ** 9 + 7)


        