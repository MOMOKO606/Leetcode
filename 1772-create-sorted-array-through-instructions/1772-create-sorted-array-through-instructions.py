class FenwickTree:
    def __init__(self, size, value):
        self.size = size
        self.tree = [value] * size

    def __lowbit(self, index):
        return index & -index

    def update(self, index, value):
        while index < self.size:
            self.tree[index] += value
            index += self.__lowbit(index)
        
    def query(self, index):
        ans = 0
        while index:
            ans += self.tree[index]
            index -= self.__lowbit(index)
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        transfer, ans = {num: i + 1 for i, num in enumerate(sorted(set(instructions)))}, 0
        ft = FenwickTree(len(transfer) + 1, 0)
        for i, num in enumerate(instructions):
            ans += min(ft.query(transfer[num] - 1), i - ft.query(transfer[num]))
            ft.update(transfer[num], 1)
        return ans % (10 ** 9 + 7)
            
        