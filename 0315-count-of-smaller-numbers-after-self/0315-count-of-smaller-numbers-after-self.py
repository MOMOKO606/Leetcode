class FenwickTree:
    def __init__(self, size, value):
        self.nodes = [value] * size
        self.size = size


    def _lowbit(self, index):
        return index & -index


    def update(self, index, delta):
        while index < self.size:
            self.nodes[index] += delta
            index += self._lowbit(index)


    def query(self, index):
        ans = 0
        while index:
            ans += self.nodes[index]
            index -= self._lowbit(index)
        return ans


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        num_to_index = {num: i + 1 for i, num in enumerate(sorted(nums))}
        ft, ans = FenwickTree(len(nums) + 1, 0), []
        for num in reversed(nums):
            i = num_to_index[num]
            ft.update(i, 1)
            ans.append(ft.query(i - 1))
        return ans[::-1]
        