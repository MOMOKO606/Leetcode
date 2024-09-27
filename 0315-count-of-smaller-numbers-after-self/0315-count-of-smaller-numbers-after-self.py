class FenwickTree:
    def __init__(self, size, value):
        self.size = size
        self.tree = [value] * size

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
    def countSmaller(self, nums: List[int]) -> List[int]:
        transfer, ans = {num: i + 1 for i, num in enumerate(sorted(set(nums)))}, []
        ft = FenwickTree(len(transfer) + 1, 0)
        for num in reversed(nums):
            i = transfer[num]
            ans.append(ft.query(i - 1))
            ft.update(i, 1)
        return ans[::-1]


        
        