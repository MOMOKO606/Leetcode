class FenwickTree:
    def __init__(self, size, original_value):
        self.size = size
        self.tree = [original_value] * size

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
        indices = {num: i + 1 for i, num in enumerate(sorted(set(instructions)))}
        ft = FenwickTree(len(indices) + 1, 0)
        ans, max_num = 0, max(instructions)
        for num in instructions:
            k = indices[num]
            ft.update(k, 1)
            ans += min(ft.query(k - 1), ft.query(indices[max_num]) - ft.query(k))
        return ans % (10 ** 9 + 7)


        